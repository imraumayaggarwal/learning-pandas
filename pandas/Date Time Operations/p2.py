import pandas as pd

# to get the day of the week, we use the method dayofweek

# we set the timestamp to that of the current time
timestamp = pd.Timestamp.now()

print(timestamp.dayofweek)
