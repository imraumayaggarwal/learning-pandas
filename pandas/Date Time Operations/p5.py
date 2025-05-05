import pandas as pd

# to check for leap year, we use the method is_leap_year

# we set the timestamp to that of the current time
timestamp = pd.Timestamp.now()

print(timestamp.is_leap_year)
