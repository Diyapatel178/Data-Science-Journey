import pandas as pd

df = pd.read_csv("students.csv")

print(df.dtypes)

df["Age"] = df["Age"].astype(float)

print(df.dtypes)