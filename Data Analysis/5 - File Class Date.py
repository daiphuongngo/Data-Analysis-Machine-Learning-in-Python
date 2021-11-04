# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 19:20:37 2019

@author: Phuong Dai Ngo
"""
# %%
"""===========================================================================
PYTHON MODULES

- Consider a module to be the same as a code library.
- A file containing a set of functions you want to include in your application.
- To create a module just save the code you want in a file with the file 
extension .py
- Now we can use the module we just created, by using the import statement
- You can create an alias when you import a module, by using the as keyword.
"""
from tutorial import day4 as d

d.test_module_day4()

# %%
"""===========================================================================
FILE HANDLING

- For file handling, we use OS module
    + use os.mkfir() to create folder
    + use os.rmdir() to delete folder
    + use os.remove() to remove file
    + use os.path.exists() to check if file exists
"""
import os

os.mkdir("F:/temp/NordicCoder/python_analysis/test_os")
os.rmdir("F:/temp/NordicCoder/python_analysis/test_os")

"""===========================================================================
- To open the file, use the built-in open() function.
- The open() function returns a file object, which has a read() method for 
reading the whole content of the file
- The open() function takes two parameters; filename, and mode.
    + "r" - Read - Default value. Opens a file for reading, error if the 
    file does not exist
    + "a" - Append - Opens a file for appending, creates the file if it 
    does not exist
    + "w" - Write - Opens a file for writing, creates the file if it 
    does not exist
    + "x" - Create - Creates the specified file, returns an error if the 
    file exists
- In addition you can specify if the file should be handled as binary or 
text mode
    + "t" - Text - Default value. Text mode
    + "b" - Binary - Binary mode (e.g. images)
"""

f = open("F:/temp/NordicCoder/python_analysis/tutorial/ggapp_sample.csv", "rt")
print(f.read())

"""===========================================================================
- You can return one line by using the readline() method.
- By looping through the lines of the file, you can read the whole file, 
line by line
- It is a good practice to always close the file when you are done with it.
"""
f = open("F:/temp/NordicCoder/python_analysis/tutorial/ggapp_sample.csv")
print(f.readline())
print(f.readline())

f = open("F:/temp/NordicCoder/python_analysis/tutorial/ggapp_sample.csv")
for x in f:
    print(x)
f.close()

"""===========================================================================
- To create a new file in Python, use the open() method, with one of the 
parameters a, w or x
- To write to an existing file, you must add parameter(a or w) to the open() 
function.
- Using write() to write content to file
- Remember to close the file
"""
file_path = "F:/temp/NordicCoder/python_analysis/tutorial/new_file.txt"
f = open(file_path, "x")

f = open(file_path, "w")
f.write("This is just some text sample")
f.close()

# %%
"""===========================================================================
PYTHON CLASSES/OBJECTS

- Python is an object oriented programming language.
- Almost everything in Python is an object, with its properties and methods.
- A Class is like an object constructor, or a "blueprint" for creating objects.
"""


# Create a Class
class MyClass:
    x = 5


# Create Object
p1 = MyClass()
print(p1.x)

"""===========================================================================
- All classes have a function called __init__(), which is always executed when 
the class is being initiated.
- Use the __init__() function to assign values to object properties, or other 
operations that are necessary to do when the object is being created.
- Objects can also contain methods. Methods in objects are functions that 
belong to the object.
- The self parameter is a reference to the current instance of the class, 
and is used to access variables that belongs to the class.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)

print(p1.name)
print(p1.age)
p1.myfunc()

# %%
"""===========================================================================
PYTHON DATES
- A date in Python is not a data type of its own, but we can import a module 
named datetime to work with dates as date objects.
- To create a date, we can use the datetime() class (constructor) of the 
datetime module.
- The datetime() class requires three parameters to create a date: year, 
month, day
- The date contains year, month, day, hour, minute, second, and microsecond.
- The datetime module has many methods to return information about the 
date object.
    + strftime() method for formatting date objects into readable strings.
        . %A: Weekday, full version
        . %Y: year, full version
        . %m: Month as a number 01-12
        . %d: Day of month 01-31
        . %H: Hour 00-23
        ....
    + strptime() for convert a string to datetime
"""
from datetime import datetime  # from module import class

x = datetime(2020, 5, 17)
x = datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
x = datetime.strptime("2019-10-16", "%Y-%m-%d")
