import pandas as pd

df = pd.read_csv("C:\\Users\\aggar\\Desktop\\students.csv")

print("DataFrame:\n\n", df)

# we have to select the column we want to apply the operation to
df['Student']= df["Student"].str.lower()

print("\n\n", df)

# we cannot select the whole dataframe as it's not allowed 