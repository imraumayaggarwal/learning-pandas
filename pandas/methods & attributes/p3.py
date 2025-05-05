import pandas as pd

data = {
    'student' : ["A", "B", "C", "D", "E"],
    'rank' : [1, 2, 4, 3, 5],
    'marks' : [27, 12, 28, 81, 98]
}

df = pd.DataFrame(data, index=['s1', 's2', 's3', 's4', 's5'])
print("student records:\n\n", df)

# returns the total no of elements present in the dataset
print("No of elements : ",df.size)