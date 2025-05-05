import pandas as pd
import numpy as np

data = [10, 20, 30, 40, 50, np.nan]

s = pd.Series(data, index = ['i1', 'i2', 'i3', 'i4', 'i5', 'i6'])

print("\nSeries :\n", s)

print("\nSeries info\n\n:  ",s.info())