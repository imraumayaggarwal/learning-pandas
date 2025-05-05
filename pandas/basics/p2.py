import pandas as pd

# dataset
data = {
    'student' : ["A", "B", "C", "D", "E"],
    'rank' : [1, 2, 4, 3, 5],
    'marks' : [27, 12, 28, 81, 98]
}

# THIS FUNCTION CREATES THE DATAFRAME (data table) AND STORES IT IN VARIABLE df
df = pd.DataFrame(data)

# PRINTS THE DATAFRAME
print("Student Records\n\n", df)

# accessing the value of a column through the index label
print("value", df.loc[1, 'marks'])