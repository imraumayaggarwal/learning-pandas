import pandas as pd

data = {
    "player" : ["amit", "john", "amit", "david", "steve", "john"],
    "rank" : [1, 4, 3, 5, 2, 7],
    "year" : [2023, 2022, 2021, 2022, 2018, 2019]
}

df = pd.DataFrame(data)

print("Dataframe")
print(df)

# grouping the data on player value and summing the ranks
res = df.groupby('player')['rank'].sum()

# displaying the first entry
print("\n", res)

# what does groupby() do?
# -> groupby() lets you group rows that have the same value in a 
#    column, and then lets you apply a function to summarize or
#    transform each group."
# functions like: sum(), mean(), count(), max() and min()

# You can also iterate over the groups to analyze each one individually.

group = df.groupby('player')
for name, grp in group:
    print("\n", name)
    print(grp)

# we can also use the function groups to see where the similar values occur
# where the output is the indices where the value is present
# example : 'Amit : [0, 2]

print("\n", df.groupby('player').groups)