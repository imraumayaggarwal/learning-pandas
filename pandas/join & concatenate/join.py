import pandas as pd

data1 = {
    'student' : ["A", "B", "C", "D", "E"],
    'id' : [1, 2, 4, 3, 5],
    'roll' : [2, 1, 8, 81, 82]
}

data2 = {
    'rank' : [12, 32, 44, 53, 25],
    'marks' : [27, 12, 28, 81, 98]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print("\nDataFrame 1:\n\n", df1)
print("\nDataFrame 2:\n\n", df2)

#joining the two dataframes
newdf = df1.join(df2)
print("\nNew Data Frame:\n\n", newdf)

# basically works for joining data frames with both DataFrames conrtaining different columns