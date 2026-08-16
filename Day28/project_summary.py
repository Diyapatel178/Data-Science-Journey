import pandas as pd

df = pd.read_csv("sales.csv")

print("===== PROJECT SUMMARY =====")
print("\nTotal sales:",df["Sales"].sum())
print("\nAvrage sales:",df["Sales"].mean())
print("\ntotal Quntity:",df["Quantity"].sum())
print("\nHighest sales product:",df.loc[df["Sales"].idxmax(),"Product"])
print("\nHighest sales city:")
city_sales = df.groupby("City")["Sales"].sum()
print(city_sales.idxmax())
