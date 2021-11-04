# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 23:35:54 2019

@author: Phuong Dai Ngo
"""

"""
REGEX
- A RegEx, or Regular Expression, is a sequence of characters that forms a 
search pattern.
- RegEx can be used to check if a string contains the specified search pattern.
    + findall() function returns a list containing all matches. If no matches 
    are found, an empty list is returned.
    + search() function searches the string for a match, and returns a Match 
    object if there is a match. If no matches are found, None is returned.
    + split() function returns a list where the string has been split at each 
    match.
    + sub() function replaces the matches with the text of your choice.
    
    
- Try, test regex pattern at: https://regex101.com/
- More regex metacharaters: https://www.w3schools.com/python/python_regex.asp
"""

import re

txt = "The rain in Spain"
x = re.findall("ain", txt)
print(x)

x = re.search("\s", txt)
print("The first white-space character is located in position: ", x.end())

x = re.split("\s", txt)
print(x)

x = re.sub("\s", "9", txt)
print(x)

txt = "all cats are smarter than dogs, all dogs are dumber than cats"
regex = r"all (.*?) are"
re.search(regex, txt)
re.findall(regex, txt)

txt = "Mr. Simon's number 0123111789, he previously used 09996677766 and recently asked to fix his phone."
regex = r"(\+1|0)([0-9]{9,10})\D"

matches = re.findall(regex, txt)
if len(matches) >= 1:
    for m in matches:
        print(m)
        print(m[0])
        print(m[1])
        
x = re.search(regex, txt)
print(x.groups())
print(x.group(0))
print(x.group(1))
print(x.group(2))
print(x.group(1, 2))


"""
DATETIME, TIMEDELTA
"""
import pandas as pd
from datetime import datetime

d = {
    "Name": pd.Series(["Tom", "James", "Ricky", "Vin", "Steve"]),
    "DoB": pd.Series(["1999-01-23", "1989-07-22 14:25:00", "1988-25-01", 
                      "2000-05-02 09:00:00", "1991/10/20 00:00:00"]),
    }

df = pd.DataFrame(d)

df["DoBDate"] = pd.to_datetime(df["DoB"], format="%Y-%m-%d %H:%M:%S.%f", errors="coerce")
df["DoBDate"] = pd.to_datetime(df["DoB"], format="%Y-%m-%d", errors="coerce")
df["Year"] = df["DoBDate"].dt.year
fil1 = df[df["DoBDate"] < datetime(1999, 1, 1)]

df["EndDate"] = df["DoBDate"] + pd.DateOffset(months=3)
df["Diff"] = df["EndDate"] - df["DoBDate"]
df["DiffMonth"] = df["Diff"].dt.days
