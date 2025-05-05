import pandas as pd

# to check last day of month, we use the method is_month_end

# we set the timestamp to that of the current time
timestamp = pd.Timestamp.now()

print(timestamp.is_month_end)
