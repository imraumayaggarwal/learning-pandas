
# 🐼 **Pandas Basics and Operations** 

Welcome to the **Pandas Basics and Operations** repository! This is a hands-on learning resource containing code files and explanations for various Pandas functionalities. The repository is organized by key topics, each demonstrating a specific Pandas feature or operation.

---

## 📂 **Folder Structure**

```bash
pandas/
    basics/
    data_cleaning/
    date_and_time_operations/
    df_operations/
        duplicates/
        insertion_and_deletion/
        iterating/
        sorting/
    join_and_concatenate/
    methods_and_attributes/
    series/
    string_operations/
    README.md
```

---

## 📌 **Sections**

### 📘 **Basics**
- **p1.py** – Creating a basic Pandas DataFrame
- **p2.py** – Accessing groups of rows and columns
- **p3.py** – Accessing rows and columns using integer positions
- **p4.py** – Renaming the indexes
- **p5.py** – Displaying columns using a loop

### 📊 **DataFrame – Attributes & Operations**

Pandas provides various built-in attributes and methods to manage DataFrames effectively.

| Attribute / Method | Description |
|--------------------|-------------|
| `dtypes`           | Return column data types |
| `ndim`             | Return the number of dimensions |
| `size`             | Total number of elements in the DataFrame |
| `shape`            | Returns the tuple of DataFrame dimensions |
| `index`            | Return the row index |
| `T`                | Transpose rows and columns |
| `head()`           | Return the first 5 rows |
| `tail()`           | Return the last 5 rows |

### 🔧 **DataFrame Operations**

#### Insertion & Deletion

- **read_csv.py**: Read a CSV file and print it.
- **assign.py**: Assign a column to the DataFrame and add it at the end.
- **insert.py**: Insert a column at a specific position in the DataFrame.
- **drop.py**: Remove rows or columns using `drop()` with `axis=0` (rows) or `axis=1` (columns).

#### Iteration Methods

- **iterrows()**: Access each row as a pandas Series.
- **itertuples()**: Access rows as tuples (faster and memory-efficient).
- **items()**: Access column name and column data as pandas Series.

#### Sorting

- **sort_values()**: Sort by column values.

For Ascending order:
```python
df.sort_values(by=['Column_name'])
```
For Descending order:
```python
df.sort_values(by=['Column_name'], ascending=False)
```

#### Handling Duplicates

- **findduplicates.py**: Use `duplicated()` to find duplicate rows.
- **removeduplicates.py**: Use `drop_duplicates()` to remove duplicates.

### 🔄 **Join & Concatenate**

- **join.py**: Join two DataFrames based on their index.
- **concatenate.py**: Concatenate DataFrames row-wise or column-wise, without worrying about matching data.


### 📅 **Date & Time Operations**

Work with dates and times in your DataFrame using Pandas' powerful date-time methods.


- **p1 :** get current date and time
- **p2 :** get the day of the week
- **p3 :** get the day of the year
- **p4 :** get the number of days in a month
- **p5 :** check if they year is a leap year
- **p6 :** check if the date is the last day of the month
- **p7 :** check if the date is the first day of the month
- **p8 :** check if the date is the last day of the year
- **p9 :** check if the date is the first day of the year

---

### 🧹 **Data Cleaning**

Data cleaning is essential for preparing your data for analysis. Common operations include:

- **isnull()**: Check for NULL values.
- **dropna()**: Remove rows with NULL values.
- **fillna()**: Replace NULL values with a specific value.
- **notnull() :** find the NOT NULL values and replace them with True

---

### 🧩 **Series**

A Pandas Series is a one-dimensional array, similar to a column in a DataFrame. Key attributes include:

***Note:** Methods & attributes of pandas series are same as what we saw in dataframes, but here are some others:*

- **copy :**  Copy of the input data
- **hasnans() :** Returns True if NaNs are in the series
- **info() :** Display the summary of the series
- **name :** names the series

---

### ✨ **String Operations**

Pandas also includes string operations that allow you to manipulate textual data in a DataFrame.

- **lower()**: Convert text to lowercase.
- **upper()**: Convert text to uppercase.
- **title()**: Convert text to title case.
- **len()**: Get the length of each string.
- **count()**: Count non-empty strings.
- **contains() :** search for a value in a column

---

### Remove Whitespace and Characters

This module demonstrates how to clean text data in Pandas by removing unwanted whitespaces or specific characters from strings.

- `strip()` – Removes leading and trailing whitespace or characters  
- `lstrip()` – Removes leading (left-side) whitespace or characters  
- `rstrip()` – Removes trailing (right-side) whitespace or characters

## 🚀 **How to Contribute**

If you'd like to contribute, feel free to fork this repository and submit a pull request with new examples, improvements, or bug fixes!

---

## 📌 **Learning Goal**

The goal of this repository is to master the **Pandas library** and effectively use it for data manipulation and cleaning. This repository will continuously evolve as I explore more advanced concepts of data science.

---

## 📚 **Resources**

You can also refer to the official Pandas documentation for in-depth details:  
[Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
