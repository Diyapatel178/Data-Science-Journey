import pandas as pd

df = pd.read_csv("sales.csv")

print(df.head())
print(df.info())
print(df.describe())
print("===== FINAL DATA ANALYSIS =====")
print("\ntotal sales:",df["Sales"].sum())
print("\nAvrage Sales:",df["Sales"].mean())
print("\nTotal Quantity:",df["Quantity"].sum())
print("\n Highest Sales product:",df.loc[df["Sales"].idxmax(),"Product"])