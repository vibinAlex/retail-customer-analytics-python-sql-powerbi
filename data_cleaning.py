"""
data_cleaning.py

Loads the raw customer shopping dataset, cleans it, engineers new
features, and loads the cleaned data into PostgreSQL via connectdb.py.
"""

import os
import pandas as pd
# from sqlalchemy import create_engine
from connectdb import conncectdbcls

# --------------------------------------------------------------------
# 1. Load the raw data
# --------------------------------------------------------------------
df = pd.read_csv(r'D:\dtafiles\customer_shopping_behavior.csv')

# df.head()

# df.info()
# RangeIndex: 3900 entries, 0 to 3899
# Data columns (total 18 columns):
#  #   Column                  Non-Null Count  Dtype
# ---  ------                  --------------  -----
#  0   Customer ID             3900 non-null   int64
#  1   Age                     3900 non-null   int64
#  2   Gender                  3900 non-null   object
#  3   Item Purchased          3900 non-null   object
#  4   Category                3900 non-null   object
#  5   Purchase Amount (USD)   3900 non-null   int64
#  6   Location                3900 non-null   object
#  7   Size                    3900 non-null   object
#  8   Color                   3900 non-null   object
#  9   Season                  3900 non-null   object
#  10  Review Rating           3863 non-null   float64   <- 37 missing
#  11  Subscription Status     3900 non-null   object
#  12  Shipping Type           3900 non-null   object
#  13  Discount Applied        3900 non-null   object
#  14  Promo Code Used         3900 non-null   object
#  15  Previous Purchases      3900 non-null   int64
#  16  Payment Method          3900 non-null   object
#  17  Frequency of Purchases  3900 non-null   object

# df.describe(include='all')
# 3,900 rows | Age 18-70 (avg ~44) | Purchase Amount avg ~$59.76
# Review Rating avg ~3.75 | most frequent Category: Clothing
df.describe(include='all')

# --------------------------------------------------------------------
# 2. Fill missing Review Rating values using the category median
# --------------------------------------------------------------------
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))

# df.isnull().sum()
# Review Rating    0     <- all 37 missing values filled
# (all other columns already had 0 missing)
df.isnull().sum()

# --------------------------------------------------------------------
# 3. Standardize column names to snake_case
# --------------------------------------------------------------------
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})
# df.columns

# --------------------------------------------------------------------
# 4. Feature engineering: age_group
# --------------------------------------------------------------------
labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)
df[['age', 'age_group']].head(10)

# --------------------------------------------------------------------
# 5. Feature engineering: purchase_frequency_days
# --------------------------------------------------------------------
df['frequency_of_purchases'].head(10)

frequency_map = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quaterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 365
}
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_map)
df[['purchase_frequency_days', 'frequency_of_purchases']].head(10)
# df.columns

# --------------------------------------------------------------------
# 6. Consistency check: discount_applied vs promo_code_used
# --------------------------------------------------------------------
# df[['discount_applied','promo_code_used']].head()
# (df['discount_applied']==df['promo_code_used']).all()   -> True, 100% match
df = df.drop('promo_code_used', axis=1)
# df.columns

# --------------------------------------------------------------------
# 7. Load the cleaned data into PostgreSQL
# --------------------------------------------------------------------
# Credentials are read from environment variables instead of being
# hardcoded, so this file is safe to commit to a public GitHub repo.
# Set these before running (e.g. in a .env file or your shell):
#   DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
username = os.getenv('DB_USERNAME', 'postgres')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST', 'localhost')
port = os.getenv('DB_PORT', '5432')
database = os.getenv('DB_NAME', 'customer_behavior')

Df = df
table_name = 'customer'

connectobj = conncectdbcls(username, password, host, port, database, Df, table_name)
connectobj.connect(username, password, host, port, database, Df, table_name)
