import pandas as pd

data = {
    "Name":["Diya","Raj","Jenil"],
    "Age":[20,21,19],
    "City":["Ahemdabad","Surat","Vadodara"]
}

df = pd.DataFrame(data)

print(df)