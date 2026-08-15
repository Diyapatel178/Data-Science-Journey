import pandas as pd
df = pd.read_csv("students.csv")

print(df.groupby("City").size())
print(df.groupby("City")["Marks"].mean())