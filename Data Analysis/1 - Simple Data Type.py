# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 23:16:23 2019

@author: Phuong Dai Ngo
"""
# %%
"""===========================================================================
INDENTATION

- Indentation refers to the spaces at the beginning of a code line.
- The indentation in Python is very important.
- Python uses indentation to indicate a block of code.   
"""
if True:
    print("this code use indentation with 4 spaces")  # print output to screen

# %%
"""===========================================================================
COMMENTS

- Comments starts with a #
"""
# this is a comment
print("hello")  # this is a comment too

# %%
"""===========================================================================
VARIABLES

- A variable is created the moment you first assign a value to it.
- A variable have Name, Type and Value.
- Coding conventions: variable naming use lower_case_with_underscores.
"""
a = 2
ho_ten = "Analysis"
bien_0 = input("Enter something: ")  # take input from user

# %%
"""===========================================================================
DATA TYPES

- In programming, data type is an important concept.
- Some of data types built-in by default in Python
    + Text Type: str
    + Numeric Types: int, float
    + Sequence Types: list, range
    + Mapping Type: dict
    + Set Type: set
    + Boolean Type: bool
    + ...
- The data type is set when you assign a value to a variable:
"""
x = "Hello World !"
x = 10
x = 10.7
x = ["Nguyen", "Ngoc", "Tu"]
x = range(8)
x = True
x = {"Ten": "Tu", "Male": True, "Age": 30}

"""===========================================================================
- Get the data type of any object by using the type() function:
"""
x = 10.7
print(type(x))

"""===========================================================================
- Setting the specific data type
"""
x = str("Hello World !")
x = int(10)
x = float(10.7)
x = list(("Nguyen", "Ngoc", "Tu"))
x = range(8)
x = bool(True)
x = dict("Ten" = "Tu", "Male" = True, "Age" = 30)

# %%
"""===========================================================================
NUMBERS

- Int: a whole number, positive or negative, without decimals.
- Float: 
    + a number, positive or negative, containing one or more decimals.
    + can also be scientific numbers with an "e" to indicate the power of 10.
- Can convert from one type to another with the int(), float() methods.
"""
x = 9
y = 9
y = float(x)  # convert int to float
x = 5.9
y = int(x)  # convert float to int
x = 700.68e-2
y = int(x)  # convert float to int

"""===========================================================================
- Casting in python using constructor functions:
    + int() - constructs an integer number from an integer literal,
        a float literal (by rounding down to the previous whole number),
        or a string literal (providing the string represents a whole number)
    + float() - constructs a float number from an integer literal,
        a float literal or a string literal (providing the string represents
        a float or an integer)
    + str() - constructs a string from a wide variety of data types,
        including strings, integer literals and float literals
"""
a = int(2.8)
a = int("3")
a = float("5.7")
a = str(3.0e3)
b = str(4.0e5)

# %%
"""===========================================================================
STRINGS

- String literals in python are surrounded by either single quotation 
marks, or double quotation marks.
- Coding conventions: using one string format for whole project
- Strings in Python are arrays of bytes representing unicode characters. 
However, Python does not have a character data type, a single character is 
simply a string with a length of 1.
- Square brackets can be used to access elements of the string.

"""
a = 'Hello World'
a = "Hello, World!"
print(a[2])
print(a[0])
print(a[1])
print(a[-4])

"""===========================================================================
- Return a range of characters by using the slice syntax: specify the start 
index and the end index, separated by a colon, to return a part of the string.
- Use negative indexes to start the slice from the end of the string:
"""
a = "Hello, World!"
print(a[2:5])
print(a[-5:-2])
print(a[-4:-1])

"""===========================================================================
* Function is a block of code to carry out a specific task, will contain its 
own scope and is called by name
* Method is somewhat similar to a function, except it is associated with 
object/classes.

- To get the length of a string, use the len() function.
- Some built-in methods that you can use on strings:
    + strip() - removes any whitespace from the beginning or the end
    + lower() - returns the string in lower case
    + upper() - returns the string in upper case
    + replace() - replaces a string with another string
    + split() - splits the string into substrings if it finds instances of 
    the separator
* Search for more string method
"""
a = "     Hello, World! "
print(len(a))
print(a.strip())
print(a.lower())
print(a.upper())
print(a.replace("H", "J"))
print(a.split(","))

"""===========================================================================
- To check if a certain phrase or character is present in a string, we can use 
the keywords in or not in.
- The find() method returns the lowest index of the substring if it is found 
in given string. If its is not found then it returns -1.
"""
txt = "The rain in Spain stays mainly in the plain"
print("ain" in txt)
print(txt.find("ain"))

"""===========================================================================
- We can combine strings and numbers by using the format() method!
- The format() method takes the passed arguments, formats them, and places 
them in the string where the placeholders {} are
- You can use index numbers {0} to be sure the arguments are placed in the 
correct placeholders
"""
quantity = 3
itemno = 567
price = 49.95

myorder = "I want to pay {} dollars for {} pieces of item {}."
print(myorder.format(quantity, itemno, price))

myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# %%
"""
BOOLEANS

- In programming you often need to know if an expression is True or False
- When you compare two values, the expression is evaluated and Python returns 
the Boolean answer
- When you run a condition in an if statement, Python returns True or False
"""
print(10 > 9)
print(10 == 9)
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

"""
- The bool() function allows you to evaluate any value, and give you True or 
False in return
- Almost any value is evaluated to True if it has some sort of content.
    + Any string is True, except empty strings.
    + Any number is True, except 0.
    + Any list, tuple, set, and dictionary are True, except empty ones.
"""
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
bool(False)
bool(None)
bool("")
bool(0)
