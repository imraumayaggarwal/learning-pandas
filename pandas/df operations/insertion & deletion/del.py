import pandas as pd

df = pd.read_csv("pandas/students.csv")

print("DataFrame:\n\n", df)
# deletes the column marks
df.drop("Marks", axis = 1, inplace=True)

print("DataFrame:\n\n", df)

# deletes the row  David
df.drop(2, axis=0, inplace=True)

print("DataFrame:\n\n", df)