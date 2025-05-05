import pandas as pd

data = [10, 20, 30, 40, 50]

s = pd.Series(data, index = ['i1', 'i2', 'i3', 'i4', 'i5'], name="NumberSeries")

print("\nSeries :\n", s)
print("\nseries Name:\n", s.name)