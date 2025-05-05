import pandas as pd

# to check first day of year, we use the method is_year_start

# we set the timestamp to that of the current time
timestamp = pd.Timestamp.now()

print(timestamp.is_year_start)
