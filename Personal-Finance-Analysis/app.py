import os
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Personal Finance Dashboard",
    page_icon="💰",
    layout="wide",
)

DATA_PATH = "data/archive/personal_finance_tracker_dataset.csv"


@st.cache_data
def load_data(path=DATA_PATH):
    if not os.path.exists(path):
        return None

    df = pd.read_csv(path)

    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
    )

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    numeric_candidates = [
        "monthly_income",
        "monthly_expense_total",
        "savings_rate",
        "budget_goal",
        "credit_score",
        "debt_to_income_ratio",
        "loan_payment",
    ]
    for col in numeric_candidates:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df.drop_duplicates().copy()


def money(value):
    if pd.isna(value):
        return "N/A"
    return f"${value:,.2f}"


df = load_data()

st.title("💰 Personal Finance & Expense Analysis")
st.caption(
    "Interactive analysis of monthly personal-finance records using "
    "Python, Pandas and NumPy."
)

if df is None:
    st.error(
        "Dataset not found. Put "
        "`personal_finance_tracker_dataset.csv` inside "
        "`data/archive/` and refresh the app."
    )
    st.stop()

required = {"monthly_expense_total"}
missing_required = required - set(df.columns)

if missing_required:
    st.error(f"Required column(s) missing: {', '.join(missing_required)}")
    st.stop()

# Sidebar filters
st.sidebar.header("🔎 Filters")

filtered = df.copy()

if "financial_scenario" in filtered.columns:
    scenarios = sorted(filtered["financial_scenario"].dropna().astype(str).unique())
    selected_scenarios = st.sidebar.multiselect(
        "Financial Scenario",
        scenarios,
        default=scenarios,
    )
    if selected_scenarios:
        filtered = filtered[
            filtered["financial_scenario"].astype(str).isin(selected_scenarios)
        ]

if "date" in filtered.columns and filtered["date"].notna().any():
    min_date = filtered["date"].min().date()
    max_date = filtered["date"].max().date()
    selected_dates = st.sidebar.date_input(
        "Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )
    if isinstance(selected_dates, tuple) and len(selected_dates) == 2:
        start, end = selected_dates
        filtered = filtered[
            (filtered["date"].dt.date >= start)
            & (filtered["date"].dt.date <= end)
        ]

# KPI cards
expense = filtered["monthly_expense_total"].dropna()

total_expense = expense.sum()
avg_expense = expense.mean()
median_expense = expense.median()
highest_expense = expense.max()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Recorded Expenses", money(total_expense))
col2.metric("Average Expense Record", money(avg_expense))
col3.metric("Median Expense", money(median_expense))
col4.metric("Highest Expense Record", money(highest_expense))

st.divider()

# Income and savings
if "monthly_income" in filtered.columns:
    income = filtered["monthly_income"].dropna()
    if not income.empty:
        c1, c2 = st.columns(2)
        c1.metric("Total Recorded Income", money(income.sum()))
        c2.metric("Average Income Record", money(income.mean()))

# Budget analysis
if {"budget_goal", "monthly_expense_total"}.issubset(filtered.columns):
    filtered["budget_variance"] = (
        filtered["budget_goal"] - filtered["monthly_expense_total"]
    )
    filtered["over_budget"] = (
        filtered["monthly_expense_total"] > filtered["budget_goal"]
    )

    st.subheader("🎯 Budget Performance")
    b1, b2, b3 = st.columns(3)
    b1.metric(
        "Over-Budget Records",
        f"{int(filtered['over_budget'].sum()):,}",
    )
    b2.metric(
        "Over-Budget %",
        f"{filtered['over_budget'].mean() * 100:.2f}%",
    )
    b3.metric(
        "Average Budget Variance",
        money(filtered["budget_variance"].mean()),
    )

# Monthly trend
if {"date", "monthly_expense_total"}.issubset(filtered.columns):
    trend = filtered.dropna(subset=["date"]).copy()
    if not trend.empty:
        trend["month"] = trend["date"].dt.to_period("M").astype(str)

        monthly = (
            trend.groupby("month")["monthly_expense_total"]
            .agg(["sum", "mean"])
            .rename(
                columns={
                    "sum": "Total Expense",
                    "mean": "Average Expense",
                }
            )
            .sort_index()
        )

        st.subheader("📈 Monthly Expense Trend")
        st.line_chart(monthly)

        highest_month = monthly["Total Expense"].idxmax()
        st.info(
            f"Highest total recorded-expense month in the selected data: "
            f"**{highest_month}** ({money(monthly.loc[highest_month, 'Total Expense'])})"
        )

# Scenario analysis
if {"financial_scenario", "monthly_expense_total"}.issubset(filtered.columns):
    st.subheader("🌍 Expense by Financial Scenario")

    scenario = (
        filtered.groupby("financial_scenario")["monthly_expense_total"]
        .agg(["count", "mean", "median", "sum"])
        .sort_values("mean", ascending=False)
    )

    scenario_display = scenario.rename(
        columns={
            "count": "Records",
            "mean": "Average Expense",
            "median": "Median Expense",
            "sum": "Total Expense",
        }
    )

    st.bar_chart(scenario_display["Average Expense"])
    st.dataframe(scenario_display, use_container_width=True)

# Savings
if "savings_rate" in filtered.columns:
    st.subheader("💵 Savings Rate")

    avg_savings = filtered["savings_rate"].mean() * 100
    median_savings = filtered["savings_rate"].median() * 100

    s1, s2 = st.columns(2)
    s1.metric("Average Savings Rate", f"{avg_savings:.2f}%")
    s2.metric("Median Savings Rate", f"{median_savings:.2f}%")

# Correlation
numeric_cols = filtered.select_dtypes(include=np.number).columns.tolist()

if len(numeric_cols) >= 2:
    st.subheader("🔗 Numeric Correlations")
    corr = filtered[numeric_cols].corr(numeric_only=True)
    st.dataframe(corr.round(2), use_container_width=True)

# Raw data
with st.expander("📄 View Filtered Data"):
    st.write(f"Showing {len(filtered):,} records")
    st.dataframe(filtered, use_container_width=True)

st.caption(
    "Note: This Kaggle dataset is synthetic and intended for teaching, "
    "research and experimentation; results should not be used for real-world "
    "financial or credit decisions."
)
