import pandas as pd

df = pd.read_csv("pandas/students.csv")

print("DataFrame:\n\n", df)

print()
for colname, col in df.items():
    print(colname)
    print(col)