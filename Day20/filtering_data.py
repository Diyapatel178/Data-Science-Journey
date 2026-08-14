import pandas as pd

df = pd.read_csv("students.csv")

print(df[df["Marks"]>85])

print(df[df["Age"]==20])