import pandas as pd

df = pd.read_csv("students.csv")

print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())

df = df.dropna()
df = df.drop_duplicates()

print(df.isnull().sum())
print(df.duplicated().sum())

print(df)
