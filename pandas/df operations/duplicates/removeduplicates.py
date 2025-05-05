import pandas as pd

data = {
    'Student': ['Amit', 'Virat', 'David', 'Will', 'Steve', 'Virat', 'Amit'],
    'Rank': [1, 2, 3, 4, 5, 2, 1],
    'Marks': [95, 90, 80, 75, 69, 90, 95]
}

df = pd.DataFrame(data)

print("DataFrame\n\n", df)

# returns in new dataframe, doesn't affect orignal
print("DataFrame\n\n", df.drop_duplicates())


