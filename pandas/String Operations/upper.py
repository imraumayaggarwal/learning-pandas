import pandas as pd

df = pd.read_csv("pandas/students.csv")

print("DataFrame:\n\n", df)

df["Student"]= df["Student"].str.upper()

print("\n\n", df)