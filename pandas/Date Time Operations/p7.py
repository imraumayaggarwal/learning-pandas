import pandas as pd

# to check first day of month, we use the method is_month_start

# we set the timestamp to that of the current time
timestamp = pd.Timestamp.now()

print(timestamp.is_month_start)
