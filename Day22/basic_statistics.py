import pandas as pd

df = pd.read_csv("students.csv")

print("avrage:",df["Marks"].mean())
print("maximum:",df["Marks"].max())
print("minimum:",df["Marks"].min())
print("Total:",df["Marks"].sum())