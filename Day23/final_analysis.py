import pandas as pd 

df = pd.read_csv("students.csv")

print("===== STUDENT PERFORMANCE ANALYSIS =====")

print("Total Student:",len(df))
print("Avrage:",df["Marks"].mean())
print("Highest Marks:",df["Marks"].max())
print("Lowest Marks:",df["Marks"].min())
print("Top student:")

top_student = df.loc[df["Marks"].idxmax()]
print(top_student)

print("Above Avarage student")
above_avrage = df[df["Marks"] > df["Marks"].mean()]
print(above_avrage)

