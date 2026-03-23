import pandas as pd
import numpy as np

df = pd.read_excel('dirty_dataset_v2.xlsx')

df = df.drop_duplicates()

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Cust_DOB'] = pd.to_datetime(df['Cust_DOB'], errors='coerce')

df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
df.loc[df['Amount'] <= 0, 'Amount'] = np.nan
df.loc[df['Amount'] > 10000, 'Amount'] = np.nan
df['Amount'] = df['Amount'].fillna(df['Amount'].median())

df['Category'] = df['Category'].str.strip().str.capitalize()
df['Status'] = df['Status'].str.strip().str.capitalize()

current_year = 2026
df['Customer_Age'] = current_year - df['Cust_DOB'].dt.year
df.loc[(df['Customer_Age'] > 100) | (df['Customer_Age'] < 0), 'Customer_Age'] = np.nan

df = df.dropna(subset=['Trans_ID', 'Date'])

df.to_csv('cleaned_dataset.csv', index=False)
print("Cleaning Complete. File saved as cleaned_dataset.csv")
