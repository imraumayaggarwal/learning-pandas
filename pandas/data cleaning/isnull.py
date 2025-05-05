import pandas as pd

df = pd.read_csv(r"C:\Users\aggar\Desktop\demo.csv")
print("Data:\n\n", df)

# returns True for null values and rest as False
res = df.isnull()

print("new data frame\n\n", res)