# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 16:26:45 2019

@author: Phuong Dai Ngo
"""

# %%
"""===========================================================================
FOR LOOPS

- A for loop is used for iterating over a sequence (that is either a list, 
a tuple, a dictionary, a set, or a string).
- With the for loop we can execute a set of statements, once for each item 
in a list, tuple, set etc.
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    x = x + "le"
    print(x)

for x in "banana":
    print(x.upper())

"""===========================================================================
- With the break statement we can stop the loop before it has looped through 
all the items
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

"""===========================================================================
- With the continue statement we can stop the current iteration of the loop, 
and continue with the next
"""
fruits = ["apple", "banana", "cherry", "orange"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

"""===========================================================================
- A nested loop is a loop inside a loop.
- The "inner loop" will be executed one time for each iteration of the 
"outer loop"
"""
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# %%
"""===========================================================================
WHILE LOOPS

- With the while loop we can execute a set of statements as long as a 
condition is true.
- While loops also have break and continue statement like for loops
- With the else statement we can run a block of code once when the condition 
no longer is true
"""

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# %%
"""===========================================================================
TRY...EXCEPT

- The try block lets you test a block of code for errors.
- The except block lets you handle the error.
- The finally block lets you execute code, regardless of the result of the 
try and except blocks.
"""
p = 3
try:
    print(p)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")


def test_module_day4():
    print("Ban dang goi function tu module day4")
