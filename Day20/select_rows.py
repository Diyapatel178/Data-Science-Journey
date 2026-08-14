import pandas as pd

df = pd.read_csv("students.csv")

print(df.iloc[0])
print(df.iloc[2])
print(df.iloc[0:2])