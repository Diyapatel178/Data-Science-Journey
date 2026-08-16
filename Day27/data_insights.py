import pandas as pd

df = pd.read_csv("sales.csv")

print("Category wise Sale:",df.groupby("Category")["Sales"].sum())
print("city wise sale:",df.groupby("City")["Sales"].sum())
print("Product wise Quntity:",df.groupby("Product")["Quantity"].sum())
