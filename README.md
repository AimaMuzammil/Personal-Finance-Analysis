# 💰 Personal Finance & Expense Analysis

An end-to-end data analysis project built with **Python, Pandas and NumPy**, with an interactive **Streamlit dashboard**.

## Dataset

This project uses Kaggle's **Personal Finance Tracker Dataset**. It contains 3,000 monthly financial records across 25 columns, including income, monthly expenses, savings rate, budget goals, financial scenario, credit score, debt-to-income ratio and loan payments.

> The dataset is synthetic and intended for teaching, research and experimentation.

## Project Goals

- Inspect and understand a real-world style CSV dataset
- Clean and prepare data
- Handle missing values and duplicates
- Convert and work with dates
- Calculate financial KPIs
- Analyze expenses and income
- Compare spending with budget goals
- Analyze savings rates
- Compare financial scenarios
- Study monthly expense trends
- Explore correlations between numeric financial variables
- Build an interactive dashboard

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit

## Project Structure

```text
Personal-Finance-Analysis/
│
├── data/
│   └── archive/
│       └── personal_finance_tracker_dataset.csv
│
├── outputs/
│   └── generated analysis files
│
├── analysis.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup in VS Code

### 1. Create and activate a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Put the dataset in the correct location

```text
data/archive/personal_finance_tracker_dataset.csv
```

### 4. Run the analysis

```bash
python analysis.py
```

The script creates analysis files inside `outputs/`.

### 5. Run the dashboard

```bash
streamlit run app.py
```

A browser window should open with the interactive dashboard.

## Main Analysis Questions

1. What is the total recorded expense?
2. What is the average and median monthly expense?
3. What is the highest expense record?
4. How does income compare with expenses?
5. How often do records exceed the budget goal?
6. What is the average savings rate?
7. How do expenses differ across financial scenarios?
8. Which month has the highest total recorded expenses?
9. Which financial variables are correlated?
10. How do the results change when dashboard filters are applied?

## Important Interpretation

Each row represents a **user's monthly financial snapshot**, not an individual transaction. Therefore, this project focuses on **monthly financial analysis** rather than transaction-level categories such as food, transport or shopping.

## Future Improvements

- Add category-level transaction data
- Add expense forecasting
- Add anomaly/fraud detection
- Add user-level financial-health segmentation
- Add machine-learning models
- Deploy the Streamlit dashboard

## Learning Outcomes

This project demonstrates practical use of:

`read_csv()` · `head()` · `info()` · `describe()` · `shape` · `isna()` · `drop_duplicates()` · `groupby()` · `sum()` · `mean()` · `median()` · `max()` · `idxmax()` · `sort_values()` · datetime operations · NumPy calculations · data visualization · Streamlit dashboards
