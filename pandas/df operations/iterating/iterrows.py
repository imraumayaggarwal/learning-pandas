import pandas as pd

df = pd.read_csv("pandas/students.csv")

print("DataFrame:\n\n", df)

print()
for row in df.iterrows():
    print(row)