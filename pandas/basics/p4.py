import pandas as pd

data = {
    'student' : ['A','B', 'C', 'D', 'E' ],
    'rank' : [1, 2, 3, 4, 5],
    'marks' : [10, 20, 30, 40, 50]
}

# RENAMING THE INDEXES
df = pd.DataFrame(data, index=('s1', 's2', 's3', 's4', 's5' ))
print(df)