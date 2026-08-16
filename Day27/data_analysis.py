import pandas as pd

df = pd.read_csv("sales.csv")

print(df.info())
print(df.describe())
print(df.isnull().sum())
print("Total sales:",df["Sales"].sum())