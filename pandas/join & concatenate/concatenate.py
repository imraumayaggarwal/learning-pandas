import pandas as pd

data1 = {
    "Id" : [100, 101, 102, 103, 104],
    "student" : ["A", "B", "C", "D", "E"],
    "roll" : [1, 2, 3, 4, 5]
}

data2 = {
    "Id" : [105, 106, 107],
    "student" : ["F", "G", "H"],
    "roll" : [6, 7, 8],
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print("Data 1\n\n", df1)
print("\nData 2\n\n", df2)

concat_df = pd.concat([df1, df2])

print("\nConcatenated DataFrame\n\n", concat_df)

#basically works when both data frames have one column in common