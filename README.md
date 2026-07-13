# retail-customer-analytics-python-sql-powerbi
End-to-end customer shopping behavior analysis using Python, PostgreSQL, and Power BI — from data cleaning to an interactive dashboard answering 10 key business questions on revenue, discounts, subscriptions, and customer segmentation.

# 🛍️ Customer Shopping Behavior Analysis

Turning 3,900 transaction records into product, pricing, and marketing insight — built with **Python**, **PostgreSQL**, and **Power BI**.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?logo=postgresql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi&logoColor=black)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## 📌 Project Overview

**Goal:** Understand purchasing patterns, customer demographics, and behavior drivers — discounts, subscriptions, shipping preferences, and purchase frequency — to support decisions on marketing, retention, and inventory.

**Pipeline:**

```
Python (cleaning & EDA)  →  PostgreSQL (storage & querying)  →  Power BI (dashboard & visualization)
```

---

## 📊 Dataset

| | |
|---|---|
| **Source file** | `customer_shopping_behavior.csv` |
| **Rows** | 3,900 transactions |
| **Columns** | 18 |
| **Missing data** | 37 values in `Review Rating` (~1%) |

**Columns include:** Customer ID, Age, Gender, Item Purchased, Category, Purchase Amount (USD), Location, Size, Color, Season, Review Rating, Subscription Status, Shipping Type, Discount Applied, Promo Code Used, Previous Purchases, Payment Method, Frequency of Purchases.

---

## 🧹 Python: Data Cleaning & EDA

1. **Load** — import the CSV with `pandas`
2. **Explore** — `df.info()` and `df.describe()` for structure and summary stats
3. **Clean** — fill 37 missing `Review Rating` values using the median rating per product category
4. **Standardize** — rename all columns to `snake_case`
5. **Feature engineer** — add `age_group` (binned ages) and `purchase_frequency_days` (derived from purchase date)
6. **Consistency check** — confirmed `discount_applied` and `promo_code_used` carried the same signal; dropped `promo_code_used` to reduce redundancy
7. **Load to database** — pushed the cleaned DataFrame into PostgreSQL for SQL analysis

---

## 🗄️ SQL: Business Questions Answered

Structured analysis performed directly in PostgreSQL:

1. Revenue by Gender
2. High-Spending Discount Users
3. Top 5 Products by Rating
4. Shipping Type Comparison
5. Subscribers vs. Non-Subscribers
6. Discount-Dependent Products
7. Customer Segmentation (New / Returning / Loyal)
8. Top 3 Products per Category
9. Repeat Buyers & Subscriptions
10. Revenue by Age Group

### Key findings

- **Revenue skews male** — Male customers generated $157,890 vs. $75,191 from female customers.
- **Express barely outsells Standard** — Avg. order value: $60.48 (Express) vs. $58.46 (Standard).
- **Non-subscribers drive more revenue** — $170,436 total vs. $62,645 from subscribers, despite similar average order size (~$59).
- **Most customers are "Loyal"** — 3,116 of 3,900 customers fall into the Loyal segment; only 83 are New and 701 Returning.

---

## 📈 Power BI Dashboard

An interactive dashboard consolidates all findings, with slicers for **subscription status, gender, category, and shipping type**.

![Dashboard](screenshots/dashboard.png)

> 📁 Add your `.pbix` file to `dashboard/` (see `dashboard/README.md`)

---

## 💡 Business Recommendations

- **Encourage More Subscriptions** — Highlight special perks to attract more customers into the subscription program.
- **Reward Loyal Customers** — Introduce a loyalty program that motivates repeat buyers to become long-term, loyal customers.
- **Reassess Discount Strategy** — Fine-tune discount offers to drive sales without cutting too deep into profit margins.
- **Strengthen Product Marketing** — Feature high-rated and top-selling items more prominently in promotional campaigns.
- **Focus Marketing Efforts** — Direct marketing resources toward age groups that generate the most revenue and customers who prefer express shipping.

---

## 🗂️ Project Structure

```
customer-shopping-behavior-analysis/
│
├── data/
│   └── customer_shopping_behavior.csv       # Raw dataset
│
├── python/
│   ├── connectdb.py                         # PostgreSQL connection class
│   └── data_cleaning.py                     # Cleaning & feature engineering
│
├── sql/
│   └── business_questions.sql               # 10 SQL business queries
│
├── dashboard/
│   └── (add your customer_behavior_dashboard.pbix here)
│
├── screenshots/
│   └── dashboard.png                        # Dashboard preview
│
├── docs/
│   ├── ProjectReport.docx                   # Full project documentation
│   └── ProjectReport.pdf
│
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

---

## ⚙️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/customer-shopping-behavior-analysis.git
cd customer-shopping-behavior-analysis
```

### 2. Set up Python environment
```bash
pip install -r requirements.txt
```

### 3. Configure database credentials
```bash
cp .env.example .env
# then edit .env with your own PostgreSQL username/password
```

### 4. Run the cleaning script
```bash
cd python
python data_cleaning.py
```
This loads `data/customer_shopping_behavior.csv`, cleans it, and pushes the result into a PostgreSQL table called `customer`.

### 5. Run the SQL business queries
```bash
psql -U <username> -d <database> -f sql/business_questions.sql
```

### 6. Open the dashboard
Open your Power BI file in `dashboard/` in Power BI Desktop and refresh the data connection.

---

## 🛠️ Tech Stack

- **Python** — pandas, numpy (data cleaning, feature engineering, EDA)
- **PostgreSQL** — data storage & business-question querying
- **Power BI** — interactive dashboard & visualization

---

## 📄 License

This project is available under the [MIT License](LICENSE).

## 🙋 Author

Feel free to reach out with questions or suggestions — contributions and feedback are welcome!

---

*The presentation for this project was created with the help of Claude AI.*
