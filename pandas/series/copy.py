import pandas as pd

data = [10, 20, 30, 40, 50]

s = pd.Series(data, index = ['i2', 'i2', 'i3', 'i4', 'i5'])

print("\nSeries :\n", s)

# copying the data
scopy = s.copy()

print(scopy)