import pandas as pd

df = pd.read_csv("C:\\Users\\aggar\\Desktop\\students.csv")

print("DataFrame:\n\n", df)

# inserts new column to desired loc = df.insert(pos,"col_name",[value])
df.insert(0, "roll", [10, 11, 12, 13, 14])

df.index = ["10" + str(i) for i in range(1, df.shape[0] + 1)]

print("DataFrame:\n\n", df)