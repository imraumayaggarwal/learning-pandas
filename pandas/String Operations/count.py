import pandas as pd

df = pd.read_csv("C:\\Users\\aggar\\Desktop\\students.csv")

print("DataFrame:\n\n", df)

# counts no of non-null values in the column
print("\n\n",df.count())

# counts no of non-null values in one column
print("\n\n",df["Student"].count())