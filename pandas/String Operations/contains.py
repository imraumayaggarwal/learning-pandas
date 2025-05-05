import pandas as pd

df = pd.read_csv("C:\\Users\\aggar\\Desktop\\students.csv")

print("DataFrame:\n\n", df)

# used to find substring in the text, also we use the case parameter here to ignore the cases
result = df["Student"].str.contains("T", case=False)

print("Answer:\n",df[result])