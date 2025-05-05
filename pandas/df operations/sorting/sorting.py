import pandas as pd

data = {
    'Student' : ["A","B","C","D","E"],
    'Roll' : [1,3,4,2,5],
    'Marks' : [84, 76, 28, 46, 27]
}

df = pd.DataFrame(data)

print("Dataframe\n\n", df)

# sorts in ascending order
df_asc = df.sort_values(by=['Roll'])
print("\nDataframe in ascending\n\n", df_asc)

# sorts in descending order
df_desc = df.sort_values(by=['Roll'], ascending=False)
print("\nDataframe in descending\n\n", df_desc)