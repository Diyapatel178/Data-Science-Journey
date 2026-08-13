import pandas as pd

data = {
    "Name": ["Diya","Aryan","Ditya","Raj"],
    "Age":[20,21,19,20],
    "Marks":[85,92,78,88],
}

df = pd.DataFrame(data)

print(df)
print(df["Name"])
print(df["Age"])
print(df["Marks"])