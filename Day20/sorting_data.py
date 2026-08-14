import pandas as pd

df = pd.read_csv("students.csv")

print(df.sort_values("Marks"))
print(df.sort_values("Marks",ascending=False))
print(df.sort_values("Age"))