import pandas as pd

data = {
    'student' : ['A', 'B', 'C', 'D', 'E'],
    'marks' : [10,20,30,40,50],
    'rank' : [1, 2, 3, 4, 5]
}

df = pd.DataFrame(data)

print(df.iloc[1,1])

# TO PRINT THE NO OF ROWS
print(df.iloc[[1,2]])