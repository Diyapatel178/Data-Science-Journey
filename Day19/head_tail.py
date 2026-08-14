import pandas as pd

df = pd.read_csv("students.csv")

print("First two row:")
print(df.head(2))

print("last two row: ")
print(df.tail(2))