import pandas as pd

df = pd.read_csv("pandas/students.csv")

print("DataFrame:\n\n", df)

# adds column to the end of the df = df.assign(col_name = [value])
newdf = df.assign(Roll = [1,2,3,4,5])

print(newdf)