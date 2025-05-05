import pandas as pd

df = pd.read_csv("pandas/demo.csv")

print("dataframe:\n\n", df)

res = df.dropna()
print("new Dataframe\n\n", res)