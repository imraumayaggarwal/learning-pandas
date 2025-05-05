import pandas as pd

data = {
    'student' : ['A','B', 'C', 'D', 'E' ],
    'rank' : [1, 2, 3, 4, 5],
    'marks' : [10, 20, 30, 40, 50]
}

df = pd.DataFrame(data)

print("student record\n", df, "\n")

# DISPLAYING columns USING ITERATION
print("\nDisplaying the columns:")
for col in df:
    print(col)