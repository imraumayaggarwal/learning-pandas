import pandas as pd

df = pd.read_csv("pandas/data.csv")

print("\n", df)

# performing the sum operation on column weight
print("\nWeight sum:\n", df['Weight'].sum())

# count of all values in the df
print("\nCount:\n", df.count())

# minimum of all columns except name
print("\nMaximum:\n", df.drop(columns = 'Name').max())

# minimum of all columns except name
print("\nMinimum:\n", df.drop(columns = 'Name').min())

# mean of all values except name
print("\nMean:\n", df.drop(columns = 'Name').mean())

# mediann of all the values except name
print("\nMeadian:\n", df.drop(columns = 'Name').median())

# standard deviation of all the values except name
print("\nStd dev:\n", df.drop(columns = 'Name').std())

# summary statistics for each column
print("\nSummary stats\n", df.describe())