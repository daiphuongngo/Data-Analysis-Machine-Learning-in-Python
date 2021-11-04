# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 23:16:36 2019

@author: Phuong Dai Ngo
"""
# %%
"""===========================================================================
OPERATORS

- Operators are used to perform operations on variables and values.
- Arithmetic operators are used with numeric values to perform common 
mathematical operations:
+, -, *, /, %, **, ...
"""
a, b = 4, 5  
print(a + b)
print(a - b)
print(a * b)

"""===========================================================================
- Assignment operators are used to assign values to variables:
=, +=, -=, *=, /=, ...
"""
a = 5
a += 3  # a = a + 3
a -= 4  # a = a - 4
a *= 1  # a = a * 1

"""===========================================================================
- Comparison operators are used to compare two values:
==, !=, >, <, <=, >=
"""
a, b = 5, 8
print(a == b)
print(a <= b)
print(a > b)

"""===========================================================================
- Logical operators are used to combine conditional statements:
and, or, not
"""
a = 5
print(a == 5 and a > 10)
print(a == 5 or a > 10)
print(not (a == 5 and a > 10))

"""===========================================================================
- Identity operators are used to compare the objects, not if they are equal, 
but if they are actually the same object, with the same memory location: 
is, is not
"""
a = 5
b = 5
print(a is b)
print(id(a))  # id() function get memory location of object
print(id(
    b))  # https://stackoverflow.com/questions/15996984/why-id-function-behaves-differently-with-integer-and-float
a = 5.5
b = 5.5
print(a is b)
print(id(a))
print(id(b))

"""===========================================================================
- Bitwise operators are used to compare (binary) numbers:
&, |, ^, ....
* Search for more
"""
a = 5
print((a == 5) & (a > 10))

# %%
"""===========================================================================
IF...ELSE

- Python logical conditions can be used in several ways, most commonly in 
"if statements" and loops.
- An "if statement" is written by using the if keyword.
- Python relies on indentation (whitespace at the beginning of a line) to 
define scope in the code.
"""
a = 33
b = 200
if b > a:
    print("b is greater than a")

"""===========================================================================
- The elif keyword is pythons way of saying "if the previous conditions were 
not true, then try this condition".
- The else keyword catches anything which isn't caught by the preceding 
conditions.
* Search for short hand if...else
"""
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

"""===========================================================================
- You can have if statements inside if statements, this is called nested if 
statements.
"""
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# %%
"""===========================================================================
FUNCTIONS

- A function is a block of code which only runs when it is called.
    + You can pass data, known as parameters, into a function.
    + A function can return data as a result.
- In Python a function is defined using the def keyword
- To call a function, use the function name followed by parenthesis
- Coding conventions: function naming use lower_case_with_underscores, should 
use word that describe function action(get_max.., calculate.., get_min.., ...)
"""


def my_function():
    print("Hello from a function")


my_function()

"""===========================================================================
- Information can be passed to functions as parameter.
- Parameters are specified after the function name, inside the parentheses. 
You can add as many parameters as you want, just separate them with a comma.
"""


def my_function(name):
    print(name + " Ngo")


my_function("Phuong")


def my_function(name, sub="Dai"):  # function can have default parameter
    print(name + " Ngo " + sub)


my_function("Phuong")
my_function(name="Phuong", sub="Dai")

"""===========================================================================
- To let a function return a value, use the return statement
"""


def my_function(x):
    return 5 * x


a = my_function(3)
print(a)
