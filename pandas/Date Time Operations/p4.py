import pandas as pd

# to get the days in a month, we use the method daysinmonth

# we set the timestamp to that of the current time
timestamp = pd.Timestamp.now()

print(timestamp.daysinmonth)
