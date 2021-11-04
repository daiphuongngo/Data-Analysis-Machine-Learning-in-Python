# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:38:02 2019

@author: Phuong Dai Ngo
"""

import pandas as pd
import numpy as np

"""===========================================================================
DATA ACQUISITION

-There are various formats for a dataset, .csv, .json, .xlsx etc. The dataset 
can be stored in different places, on your local machine or sometimes online.
- Example data: https://archive.ics.uci.edu/ml/datasets/automobile
- We use pandas.read_csv() function to read the csv file.
- Some method:
    + .head(n): show top n rows of the dataframe
    + .tail(n): show bottom n rows
    + .sample(n): show randomly n rows
"""
path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/" \
       "CognitiveClass/DA0101EN/auto.csv"
df = pd.read_csv(path, header=None)
# temp = df[0]

df.head(5)
df.sample(10)

"""===========================================================================
- When read_csv, pandas automatically set the header by row 0, since this data
don"t have a header, we add header=None when read_csv
- Then we can add headers manually, create a list "headers" that include all 
column names in order. Then, we use dataframe.columns = headers to replace the 
headers by the list we created.

"""
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration",
           "num-of-doors", "body-style", "drive-wheels", "engine-location",
           "wheel-base", "length", "width", "height", "curb-weight",
           "engine-type", "num-of-cylinders", "engine-size", "fuel-system",
           "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm",
           "city-mpg", "highway-mpg", "price"]
df.columns = headers
df.head(10)

"""===========================================================================
- We can save the dataset to csv by using the dataframe.to_csv() method.
- We can also read/save other data format:
    + csv: pd.read_csv() | pd.to_csv()
    + json: pd.read_json() | pd.to_json()
    + excel: pd.read_excel() | pd.to_excel()
    + ...    
"""
df.to_csv("F:/temp/NordicCoder/python_analysis/automobile.csv", index=False)

# %%
"""===========================================================================
BASIC INSIGHT OF DATASET

-Data has a variety of types.
The main types stored in Pandas dataframes are object, float, int, bool and 
datetime64. In order to better learn about each attribute, it is always good 
for us to know the data type of each column
- Some method:
    + .describe(): statistical summary of each column, such as count, column 
    mean value, column standard deviation, ...
    + .info(): another method you can use to check your dataset
"""
df.dtypes
temp = df.describe()
df.info()
df.shape

"""===========================================================================
- A column in a DataFrame can be retrieved as a Series either by dict-like 
notation or by attribute
"""
temp = df["make"]
temp = df.symboling
temp = df[["make", "symboling"]]

"""===========================================================================
- Rows can also be retrieved by position or name by a couple of methods, 
such as the ix indexing field

"""
temp = df.ix[0]
print(temp["symboling"])
print(temp[1])
print(temp["make"])
print(temp[3])

temp = df.ix[1:4]

temp = df.ix[:2, 2:]
temp = df.ix[[0, 2], ["make", "symboling"]]

temp = df.iloc[:2, 2:]
temp = df.iloc[[0, 2], [0, 1]]
temp = df.loc[[0, 2], ["make", "symboling"]]
"""===========================================================================
- Columns can be modified by assignment
- When assigning lists or arrays to a column, the value’s length must match 
the length of the DataFrame
- Assigning a column that doesn’t exist will create a new column
- The del keyword will delete columns 
"""
df["add1"] = 10.5

df["add1"] = np.arange(205)
del df["add1"]

"""===========================================================================
- The drop method will return a new object with the indicated value or 
values deleted from an axis
"""
temp = df.drop(1)
temp = df.drop(["make", "symboling"], axis=1)

"""===========================================================================
- To rename columns, we can assign a new list headers or use .rename()
"""
df2 = df.copy()
df2.columns.tolist()

df2.rename(columns={"normalized-losses": "normalized_losses",
                    "fuel-type": "fuel_type", "make": "branch"}, inplace=True)

df2.columns = df2.columns.str.replace("-", "_")

# %%
"""===========================================================================
IDENTIFY MISSING VALUES
- In the car dataset, missing data comes with the question mark "?". We 
replace "?" with NaN (Not a Number), which is Python"s default missing value 
marker, for reasons of computational speed and convenience. 
Here we use the function .replace(A, B, inplace = True) 

"""
# replace "?" to NaN
df.replace("?", np.nan, inplace=True)
df.head(5)
df.info()
"""===========================================================================
- The missing values are converted to Python"s default. We use Python"s built-in 
functions to identify these missing values. 
- There are two methods to detect missing data:
    + .isnull()
    + .notnull()
- "True" stands for missing value, while "False" stands for not missing value.
"""
missing_data = df.isnull()
missing_data.head(5)
missing_data = df.isnull().any(axis=0)

"""===========================================================================
Using a for loop in Python, we can quickly figure out the number of missing 
values in each column. As mentioned above, "True" represents a missing value, 
"False" means the value is present in the dataset. In the body of the for loop 
the method ".value_counts()" counts the number of "True" values.

"""
for column in missing_data.columns.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("-----")

temp = df["make"].value_counts()
df[["make", "fuel-type"]].nunique()

"""===========================================================================
Deal with missing data
- drop data
    + drop the whole row
    + drop the whole column
- replace data
    + replace it by mean
    + replace it by frequency
    + replace it based on other functions

- Whole columns should be dropped only if most entries in the column are empty. 
In our dataset, none of the columns are empty enough to drop entirely. We 
have some freedom in choosing which method to replace data; however, some 
methods may seem more reasonable than others.
"""
avg_horsepower = df["horsepower"].astype("float").mean(axis=0)

print("Average horsepower:", avg_horsepower)
df["horsepower"].replace(np.nan, avg_horsepower, inplace=True)

avg_bore = df["bore"].astype("float").mean(axis=0)
print("Average of bore:", avg_bore)
df["bore"].replace(np.nan, avg_bore, inplace=True)

df["num-of-doors"].value_counts()
df["num-of-doors"].value_counts().idxmax()

#check = df[df["num-of-doors"].isnull()]
#df[df["body-style"] == "sedan"]["num-of-doors"].value_counts()

# replace the missing "num-of-doors" values by the most frequent
df["num-of-doors"].replace(np.nan, "four", inplace=True)

# simply drop whole row with NaN in "price" column
df.dropna(subset=["price"], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)

# %%
"""===========================================================================
CORRECT DATA FORMAT
- Checking and making sure that all data is in the correct format (int, float, 
text or other), we use:
    + .dtype to check the data type
    + .astype() to change the data type

"""
df["horsepower"].dtype
df["horsepower"] = df["horsepower"].astype(float)
df.dtypes

# %%
"""===========================================================================
DATA STANDARDIZATION
- Data is usually collected from different agencies with different formats.
- Standardization is the process of transforming data into a common format 
which allows the researcher to make the meaningful comparison.
- In our dataset, the fuel consumption columns "city-mpg" and "highway-mpg" 
are represented by mpg (miles per gallon) unit. Assume we are developing an 
application in a country that accept the fuel consumption with L/100km standard
- We will need to apply data transformation to transform mpg into L/100km?
"""
# Convert mpg to L/100km by mathematical operation (235 divided by mpg)
df["city-lpk"] = 235 / df["city-mpg"]
df["city-lpk"] = round(df["city-lpk"], 2)

df["highway-lpk"] = round(235 / df["highway-mpg"], 2)
df["total-lpk"] = (df["city-lpk"] + df["highway-lpk"]) / 2
df["total-lpk2"] = df[["city-lpk", "highway-lpk"]].sum(axis=1)
df["total-lpk2"] = df[["city-lpk", "highway-lpk"]].mean(axis=1)

# %%
"""===========================================================================
DATA NORMALIZATION
- Normalization is the process of transforming values of several variables 
into a similar range. EX: scaling the variable so the variable average is 0,
scaling variable so the variable values range from 0 to 1.
"""
# replace (original value) by (original value)/(maximum value)
df["length"] = df["length"] / df["length"].max()
df["width"] = df["width"] / df["width"].max()

# %%
"""===========================================================================
BINNING
- Binning is a process of transforming continuous numerical variables into 
discrete categorical "bins", for grouped analysis.
EX: In our dataset, "horsepower" is a real valued variable ranging from 48 to 
288, it has 57 unique values. What if we only care about the price difference 
between cars with high horsepower, medium horsepower, and little horsepower 
(3 types)?

"""
from matplotlib import pyplot as plt

df["horsepower"] = df["horsepower"].astype(float)
plt.hist(df["horsepower"])

# set x/y labels and plot title
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")

bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
group_names = ["Low", "Medium", "High"]

df["horsepower-binned"] = pd.cut(df["horsepower"], bins, labels=group_names,
                                 include_lowest=True)
df["horsepower-binned"].value_counts()

# %%
"""===========================================================================
DUMMY VARIABLE
- An indicator variable (or dummy variable) is a numerical variable used to 
label categories. They are called "dummies" because the numbers themselves 
don"t have inherent meaning.
EX: We see the column "fuel-type" has two unique values, "gas" or "diesel". 
Regression doesn"t understand words, only numbers. To use this attribute in 
regression analysis, we convert "fuel-type" into indicator variables.
"""
dummy = pd.get_dummies(df["fuel-type"], prefix="fuel")
dummy.head()
# merge data frame "df" and "dummy_variable_1"
df = pd.merge(df, dummy.iloc[:, 1:], left_index=True, right_index=True)
# df = pd.concat([df, dummy.iloc[:,1:]], axis=1)
df.drop("fuel-type", axis=1, inplace=True)

# %%
"""===========================================================================
FILTERING
- We can filter rows of a DataFrame by column value
"""
print(df["body-style"].value_counts())
temp = df[df["body-style"] == "sedan"]
temp = df[df["body-style"].isin(["sedan", "hatchback"])]
temp = df[df["city-mpg"] > 20]
temp = df[(df["city-mpg"] > 20) & (df["body-style"] == "sedan")]
temp = df[(df["city-mpg"] > 20) | (df["body-style"] == "sedan")]

# why can"t use and/or, check https://stackoverflow.com/questions/21415661/logical-operators-for-boolean-indexing-in-pandas
