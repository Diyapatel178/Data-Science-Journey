import pandas as pd

df = pd.read_csv("students.csv")

print("Avarage:",df["Marks"].mean())
print("Maximum:",df["Marks"].max())
print("Minimum:",df["Marks"].min())
print("Total:",df["Marks"].sum())

print(df.groupby("City").size())
print(df.groupby("City")["Marks"].mean())

print("student with marks above 80:")
print(df[df["Marks"]>80])

print("student sorted by marks:")
print(df.sort_values("Marks",ascending=False))

top_student = df.loc[df["Marks"].idxmax()]
print("Top Student:",top_student)

above_avrage = df[df["Marks"]> df["Marks"].mean()]
print("Above avrage student:",above_avrage)