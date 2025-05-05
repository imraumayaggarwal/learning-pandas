import pandas as pd

df = pd.read_csv("pandas/demo.csv")
print("Dataframe\n\n", df)


# returns the not null data as True and rest all as False
res = df.notnull()
print("New dataframe\n\n", res)
