import pandas as pd

df = pd.read_csv("students.csv")

print(df["Marks"].agg(["mean","max","min","sum","count"]))