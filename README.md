# 💰 Personal Finance & Expense Analysis

A complete **data analysis and visualization project** built with **Python, Pandas, NumPy, Matplotlib, Seaborn, and Streamlit**.

This project explores a synthetic personal finance dataset to understand **income, expenses, savings, budgets, financial scenarios, and relationships between financial variables**. It also includes an interactive Streamlit dashboard for exploring the data through filters and visualizations.

---

## 📊 Project Overview

The goal of this project is to take a raw financial dataset, clean and analyze it, extract meaningful insights, and present the results through an interactive dashboard.

The project covers the complete data analysis workflow:

**Raw Dataset → Data Cleaning → Exploration → Analysis → Visualization → Interactive Dashboard**

---

## ✨ Features

- 📥 Load and inspect financial data using Pandas
- 🧹 Handle missing values and duplicate records
- 📅 Convert and work with date information
- 💰 Analyze income and monthly expenses
- 📊 Calculate financial KPIs
- 🎯 Compare expenses with budget goals
- 💾 Analyze savings rates
- 📈 Analyze monthly expense trends
- 🔎 Compare expenses across financial scenarios
- 🔗 Explore correlations between numeric variables
- 📊 Generate analysis output files
- 🖥️ Interactive Streamlit dashboard
- 🎛️ Dashboard filters for exploring different subsets of the data

---

## 📁 Dataset

The project uses Kaggle's **Personal Finance Tracker Dataset**.

The dataset contains **3,000 monthly financial records across 25 columns**, including information such as:

- Income
- Monthly expenses
- Savings rate
- Budget goals
- Financial scenario
- Credit score
- Debt-to-income ratio
- Loan payments
- Date information

> **Note:** The dataset is synthetic and intended for teaching, research, and experimentation.

Each row represents a **user's monthly financial snapshot**, not an individual transaction. Therefore, this project focuses on monthly financial analysis rather than transaction-level categories such as food, transport, or shopping.

---

## 🔍 Analysis Performed

### 1. Data Understanding

The dataset was initially inspected to understand:

- Number of rows and columns
- Column names
- Data types
- Missing values
- Duplicate records
- Statistical summaries

### 2. Data Cleaning

The analysis includes:

- Missing-value detection and handling
- Duplicate detection and removal
- Date conversion
- Data preparation for analysis

### 3. Financial Analysis

The project analyzes:

- Total recorded expenses
- Average monthly expense
- Median monthly expense
- Highest expense record
- Income vs. expenses
- Savings rates
- Budget performance
- Financial scenarios
- Monthly expense trends

### 4. Correlation Analysis

Numeric financial variables are analyzed to identify relationships between factors such as:

- Income
- Expenses
- Savings
- Budget goals
- Credit score
- Debt-related variables
- Loan payments

### 5. Scenario Analysis

Expenses are compared across different **financial scenarios** to understand how spending patterns vary.

---

## 📊 Interactive Dashboard

The project includes a **Streamlit dashboard** that makes the analysis interactive.

The dashboard allows users to explore financial data using filters and view different financial metrics and visualizations.

### Dashboard includes:

- Financial KPIs
- Expense analysis
- Income and expense comparisons
- Savings analysis
- Budget analysis
- Scenario comparisons
- Monthly trends
- Correlation analysis
- Interactive filters

---

## 🛠️ Tech Stack

| Technology     | Purpose                                   |
| -------------- | ----------------------------------------- |
| **Python**     | Core programming and analysis             |
| **Pandas**     | Data cleaning, manipulation, and analysis |
| **NumPy**      | Numerical calculations                    |
| **Matplotlib** | Data visualization                        |
| **Seaborn**    | Statistical visualization                 |
| **Streamlit**  | Interactive dashboard                     |

---

## 📂 Project Structure

```text
Personal-Finance-Analysis/
│
├── data/
│   └── archive/
│       ├── README.txt
│       └── personal_finance_tracker_dataset.csv
│
├── outputs/
│   └── .gitkeep
│
├── analysis.py
├── app.py
├── requirements.txt
├── README.md
├── run_project.bat
└── .gitignore
```

> Analysis output CSV files are generated locally when `analysis.py` is executed and are intentionally excluded from Git tracking.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/AimaMuzammil/Personal-Finance-Analysis.git
cd Personal-Finance-Analysis
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

### 3. Activate the virtual environment

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the analysis

```bash
python analysis.py
```

The analysis generates output files inside the `outputs/` directory.

### 6. Run the Streamlit dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser.

---

## 🧠 Main Analysis Questions

This project investigates questions such as:

1. What is the total recorded expense?
2. What is the average and median monthly expense?
3. What is the highest expense record?
4. How does income compare with expenses?
5. How often do records exceed the budget goal?
6. What is the average savings rate?
7. How do expenses differ across financial scenarios?
8. Which month has the highest total recorded expenses?
9. Which financial variables are correlated?
10. How do results change when dashboard filters are applied?

---

## 📚 Pandas & Data Analysis Concepts Used

This project demonstrates practical use of:

```text
read_csv()
head()
info()
describe()
shape
isna()
drop_duplicates()
groupby()
sum()
mean()
median()
max()
idxmax()
sort_values()
```

It also uses:

- DateTime operations
- NumPy calculations
- Data aggregation
- Data filtering
- Statistical analysis
- Data visualization
- Correlation analysis
- Streamlit dashboard development

---

## 🎯 Learning Outcomes

Through this project, I practiced the complete data-analysis workflow:

**Data Collection → Data Understanding → Data Cleaning → Data Exploration → Statistical Analysis → Visualization → Dashboard Development**

The project strengthened practical skills in **Python, Pandas, NumPy, data visualization, exploratory data analysis, and Streamlit**.

---

## 🔮 Future Improvements

Possible future improvements include:

- 📊 Add category-level transaction data
- 🔮 Add expense forecasting
- 🚨 Add anomaly detection
- 👤 Add financial-health segmentation
- 🤖 Add machine-learning models
- ☁️ Deploy the Streamlit dashboard
- 📈 Add more advanced financial visualizations

---

## 👩‍💻 Author

**Aima Muzammil**

GitHub: [@AimaMuzammil](https://github.com/AimaMuzammil)

---

⭐ If you find this project useful, feel free to explore the repository and the analysis.
