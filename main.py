# Imports

import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import BytesIO

# ============================
# 1️⃣ DIRECT CSV FILES
# ============================

def load_csv_to_df(url, name):
    response = requests.get(url)
    if response.status_code == 200:
        df = pd.read_csv(BytesIO(response.content))
        print(f"\n✅ [{name}] Preview:")
        print(df.head())
        return df
    else:
        print(f"❌ Failed to load {name}: {url}")
        return None

# Public Debt CSV
load_csv_to_df(
    'https://www.centralbank.go.ke/uploads/government_finance_statistics/42346012_Public%20Debt.csv',
    'Public Debt'
)

# Revenue & Expenditure CSV
load_csv_to_df(
    'https://www.centralbank.go.ke/uploads/government_finance_statistics/1142265704_Revenue%20and%20Expenditure.csv',
    'Revenue & Expenditure'
)

# Domestic Debt by Instrument CSV
load_csv_to_df(
    'https://www.centralbank.go.ke/uploads/government_finance_statistics/1296385373_Domestic%20Debt%20by%20Instrument.csv',
    'Domestic Debt by Instrument'
)

# Monthly Exchange Rates CSV
load_csv_to_df(
    'https://www.centralbank.go.ke/uploads/exchange_rates/444703643_Monthly%20exchange%20rate%20(end%20period).csv',
    'Monthly Exchange Rates'
)

# ============================
# 2️⃣ SCRAPED HTML TABLES
# ============================

def scrape_cbk_table_to_df(url, name):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')
        rows = []
        for row in table.find_all('tr'):
            cols = [ele.text.strip() for ele in row.find_all(['td', 'th'])]
            rows.append(cols)
        df = pd.DataFrame(rows)
        df.columns = df.iloc[0]  # first row as header
        df = df[1:]  # data only
        print(f"\n✅ [{name}] Preview:")
        print(df.head())
        return df
    else:
        print(f"❌ Failed to scrape {name}: {url}")
        return None

# Annual GDP
scrape_cbk_table_to_df(
    'https://www.centralbank.go.ke/annual-gdp/',
    'Annual GDP'
)

# Inflation Rates
scrape_cbk_table_to_df(
    'https://www.centralbank.go.ke/inflation-rates/',
    'Inflation Rates'
)

# Foreign Trade Summary
scrape_cbk_table_to_df(
    'https://www.centralbank.go.ke/foreign-trade-summary/',
    'Foreign Trade Summary'
)

# Commercial Banks Weighted Average Rates
scrape_cbk_table_to_df(
    'https://www.centralbank.go.ke/commercial-banks-weighted-average-rates/',
    'Commercial Banks Rates'
)


print("\n✅✅✅ ALL data successfully collected & previewed — ready for ETL stage!")



