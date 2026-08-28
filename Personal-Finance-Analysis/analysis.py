import os
import numpy as np
import pandas as pd

DATA_PATH = "data/archive/personal_finance_tracker_dataset.csv"
OUTPUT_DIR = "outputs"


def load_data(path=DATA_PATH):
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Dataset not found at: {path}\n"
            "Download personal_finance_tracker_dataset.csv from Kaggle "
            "and place it in data/archive/."
        )

    df = pd.read_csv(path)

    # Clean column names
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
    )

    # Convert date when available
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Convert common numeric columns
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

    return df


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    df = load_data()

    print("\n========== PERSONAL FINANCE ANALYSIS ==========\n")

    print("Shape:", df.shape)
    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nData types and non-null values:")
    df.info()

    print("\nMissing values:")
    print(df.isna().sum().sort_values(ascending=False))

    print("\nDuplicate rows:", df.duplicated().sum())

    print("\nDescriptive statistics:")
    print(df.describe(include="all").transpose())

    # Remove exact duplicate rows for analysis
    clean_df = df.drop_duplicates().copy()

    # Basic financial KPIs
    if "monthly_expense_total" in clean_df.columns:
        expenses = clean_df["monthly_expense_total"].dropna()
        print("\n--- Expense KPIs ---")
        print("Total recorded expenses:", round(expenses.sum(), 2))
        print("Average monthly expense record:", round(expenses.mean(), 2))
        print("Median monthly expense:", round(expenses.median(), 2))
        print("Highest monthly expense record:", round(expenses.max(), 2))
        print("Lowest monthly expense record:", round(expenses.min(), 2))

    if "monthly_income" in clean_df.columns:
        income = clean_df["monthly_income"].dropna()
        print("\nTotal recorded income:", round(income.sum(), 2))
        print("Average monthly income record:", round(income.mean(), 2))

    # Budget analysis
    if {"budget_goal", "monthly_expense_total"}.issubset(clean_df.columns):
        clean_df["budget_variance"] = (
            clean_df["budget_goal"] - clean_df["monthly_expense_total"]
        )
        clean_df["over_budget"] = clean_df["monthly_expense_total"] > clean_df["budget_goal"]

        print("\n--- Budget Analysis ---")
        print("Records over budget:", int(clean_df["over_budget"].sum()))
        print("Over-budget percentage:",
              round(clean_df["over_budget"].mean() * 100, 2), "%")
        print("Average budget variance:",
              round(clean_df["budget_variance"].mean(), 2))

    # Savings analysis
    if "savings_rate" in clean_df.columns:
        print("\n--- Savings Analysis ---")
        print("Average savings rate:",
              round(clean_df["savings_rate"].mean() * 100, 2), "%")
        print("Median savings rate:",
              round(clean_df["savings_rate"].median() * 100, 2), "%")

    # Scenario analysis
    if {"financial_scenario", "monthly_expense_total"}.issubset(clean_df.columns):
        scenario_expense = (
            clean_df.groupby("financial_scenario")["monthly_expense_total"]
            .agg(["count", "mean", "median", "sum"])
            .sort_values("mean", ascending=False)
        )
        print("\n--- Expense by Financial Scenario ---")
        print(scenario_expense)
        scenario_expense.to_csv(f"{OUTPUT_DIR}/scenario_expense_summary.csv")

    # Date analysis
    if {"date", "monthly_expense_total"}.issubset(clean_df.columns):
        clean_df["month"] = clean_df["date"].dt.to_period("M").astype(str)

        monthly = (
            clean_df.groupby("month")
            .agg(
                total_expense=("monthly_expense_total", "sum"),
                average_expense=("monthly_expense_total", "mean"),
                records=("monthly_expense_total", "size"),
            )
            .sort_index()
        )

        print("\n--- Monthly Expense Summary ---")
        print(monthly)

        monthly.to_csv(f"{OUTPUT_DIR}/monthly_expense_summary.csv")

        if not monthly.empty:
            highest_month = monthly["total_expense"].idxmax()
            print("\nHighest total recorded-expense month:", highest_month)

    # Category-like columns: analyze any low-cardinality categorical columns
    categorical_cols = clean_df.select_dtypes(include="object").columns.tolist()
    print("\nCategorical columns:", categorical_cols)

    # Correlation among useful numeric financial variables
    numeric_cols = clean_df.select_dtypes(include=np.number).columns.tolist()
    if len(numeric_cols) >= 2:
        corr = clean_df[numeric_cols].corr(numeric_only=True)
        corr.to_csv(f"{OUTPUT_DIR}/numeric_correlations.csv")
        print("\nCorrelation matrix saved to outputs/numeric_correlations.csv")

    # Save cleaned dataset
    clean_df.to_csv(f"{OUTPUT_DIR}/cleaned_finance_data.csv", index=False)

    print("\nFiles saved in outputs/:")
    print("- cleaned_finance_data.csv")
    print("- scenario_expense_summary.csv (when scenario columns exist)")
    print("- monthly_expense_summary.csv (when date + expense columns exist)")
    print("- numeric_correlations.csv (when enough numeric columns exist)")
    print("\nAnalysis complete.")


if __name__ == "__main__":
    main()
