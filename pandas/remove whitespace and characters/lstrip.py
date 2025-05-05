import pandas as pd

data = {'Name' : ["!Amit", "Havells\n", "Nathan\t"]}
df = pd.DataFrame(data)
print("Dataframe :\n\n", df)

# removes the whitespaces and specific characters
print("\n\nAfter using strip()\n", df['Name'].str.lstrip("\n\t!"))

