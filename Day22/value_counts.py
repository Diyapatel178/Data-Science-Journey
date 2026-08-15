import pandas as pd

df = pd.read_csv("students.csv")

print(df["City"].value_counts())
print(df["Age"].value_counts())