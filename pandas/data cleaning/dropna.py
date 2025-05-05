import pandas as pd

df = pd.read_csv(r"C:\Users\aggar\Desktop\demo.csv")

print("dataframe:\n\n", df)

res = df.dropna()
print("new Dataframe\n\n", res)