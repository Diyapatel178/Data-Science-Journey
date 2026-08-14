import pandas as pd

df = pd.read_csv("students.csv")

df.rename(
    columns={
        "Name":"Student_Name",
        "Marks":"Student_Marks"
    },
    inplace=True

)

print(df)