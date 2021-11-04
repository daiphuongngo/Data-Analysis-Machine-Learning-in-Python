# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:12:54 2019

@author: Phuong Dai Ngo
"""
import pandas as pd
import numpy as np

"""===========================================================================
FUNCTION APPLICATION
- Functions can be applied along the axes of a DataFrame using the apply() 
method.
"""
df = pd.DataFrame(np.random.randn(5, 3), columns=["col1", "col2", "col3"])
print(df.apply(np.mean))
print(df.apply(np.mean, axis=1))

# APPLY YOUR OWN FUNCTION
d = {
    "Name": pd.Series(["Tom", "James", "Ricky", "Vin", "Steve", "Smith", "Jack",
                       "Lee", "David", "Gasper", "Betina", "Andres"]),
    "Age": pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
    "Rating": pd.Series(
        [4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])
    }
df = pd.DataFrame(d)


def gom_tuoi(row):
    #    row["nhom_tuoi"] = ""
    print("=====")
    print(type(row))
    print(type(row["Age"]))
    if row["Age"] < 30:
        row["nhom_tuoi"] = "Tre"
    elif 30 <= row["Age"] <= 50:
        row["nhom_tuoi"] = "Trung nien"
    elif row["Age"] > 50:
        row["nhom_tuoi"] = "Lon tuoi"
    return row


df_new = df.apply(gom_tuoi, axis=1)

d = {"col1": pd.Series([1, 2, 3, 4, 5]),
    "col2": pd.Series([100, 200, 300, 400, 500])}

"""
ITERATING A DATAFRAME
+ iteritems() − to iterate over the (key,value) pairs
+ iterrows() − iterate over the rows as (index,series) pairs

"""
df = pd.DataFrame(np.random.randn(4, 3), columns=["col1", "col2", "col3"])
for key, value in df.iteritems():
    print(key)
    print(value)

for row_index, row in df.iterrows():
    print(row_index)
    print(row)

"""
- Using the sort_index() method, by passing the axis arguments and the order of 
sorting, DataFrame can be sorted
- sort_values() is the method for sorting by values
"""
unsorted_df = pd.DataFrame(np.random.randn(10, 2),
                           index=[1, 4, 6, 2, 3, 5, 9, 8, 0, 7],
                           columns=["col2", "col1"])

unsorted_df.sort_index()

unsorted_df.sort_index(ascending=False)

unsorted_df.sort_index(axis=1)

unsorted_df.sort_values(by="col1")

"""
GROUP BY
- Any groupby operation involves one of the following operations on the 
original object:
    + Splitting the Object
    + Applying a function
    + Combining the results
"""
ipl_data = {"Team": ["Riders", "Riders", "Devils", "Devils", "Kings",
                     "kings", "Kings", "Kings", "Riders", "Royals", "Royals",
                     "Riders"],
            "Rank": [1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2],
            "Year": [2014, 2015, 2014, 2015, 2014, 2015, 2014, 2015, 2014, 2014,
                     2015, 2015],
            "Points": [876, 789, 863, 673, 741, 812, 756, 788, 694, 701, 804,
                       690]}
df = pd.DataFrame(ipl_data)

print(df.groupby("Team"))
print(df.groupby("Team").groups)
print(df.groupby(["Team", "Year"]).groups)

grouped = df.groupby("Team")
for name, group in grouped:
    print(name)
    print(group)
print(grouped.get_group(("Devils", 2014)))

grouped = df.groupby("Team")
print(grouped["Points"].agg(np.sum))
print(grouped["Points"].agg([np.sum, np.mean, np.std]))

new_df = grouped["Points"]["Year"]()

"""
MERGE, CONCAT
- use .merge() function to join DataFrame, similar to standard database join 
operations
- use .concat() function to combine together DataFrame
"""

left = pd.DataFrame({
    "left_id": [1, 2, 3, 4, 5],
    "Name": ["Alex", "Amy", "Allen", "Alice", "Ayoung"],
    "subject_id": ["sub1", "sub2", "sub4", "sub6", "sub5"]})
right = pd.DataFrame(
    {"right_id": [1, 2, 3, 4, 5],
     "Name": ["Amy", "Brian", "Bran", "Bryce", "Betty"],
     "subject_id": ["sub2", "sub4", "sub3", "sub6", "sub5"]})

print(pd.merge(left, right, on=["Name", "subject_id"]))
print(pd.merge(left, right, on="subject_id", how="left"))
print(pd.merge(left, right, on="subject_id", how="outer"))
print(pd.merge(left, right, left_on="left_id", right_on="right_id"))

#temp.reset_index(inplace=True)
