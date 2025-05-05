import pandas as pd

df = pd.read_csv("pandas/demo.csv")

print("Dataframe :\n\n", df)

res = df.fillna(2222)
print("New dataframe\n\n", res)