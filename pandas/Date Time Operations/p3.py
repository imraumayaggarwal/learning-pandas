import pandas as pd

# to get the day of the year, we use the method dayofyear

# we set the timestamp to that of the current time
timestamp = pd.Timestamp.now()

print(timestamp.dayofyear)
