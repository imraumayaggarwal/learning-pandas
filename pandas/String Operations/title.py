import pandas as pd

data = {
    'Name' : ["amit", "rahul", "shivam", "saresh"]
}
df = pd.DataFrame(data)
print("DataFrame\n\n", df)

# converts to the camel case
df["Name"] = df["Name"].str.title()
print("DataFrame\n\n", df)