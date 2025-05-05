import pandas as pd

# to check last day of year, we use the method is_year_end

# we set the timestamp to that of the current time
timestamp = pd.Timestamp.now()

print(timestamp.is_year_end)
