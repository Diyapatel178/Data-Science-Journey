import pandas as pd

df = pd.read_csv("sales.csv")

print("===== SALES ANALYSIS REPORT =====")
print("\nTotal sales:",df["Sales"].sum())

print("\nHighest sales category:")
category_sales = df.groupby("Category")["Sales"].sum()
print(category_sales.idxmax())

print("Highest Sales City:")
City_sales = df.groupby("City")["Sales"].sum()
print(City_sales.idxmax())

print("Highest Quantity Product:")
product_quantity = df.groupby("Product")["Quantity"].sum()
print(product_quantity.idxmax())