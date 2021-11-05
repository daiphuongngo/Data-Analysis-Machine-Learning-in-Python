# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 10:48:37 2020

@author: Phuong Dai Ngo
"""

"""============================================================================
1. Write a function to input 2 numbers, print out the greater one
"""
def compare_2numbers(number1, number2):
    if number1 > number2:
        print(number1)
    elif number2 > number1:
        print(number2)
compare_2numbers(9, 7)


def compare_2numbers_method2(number1, number2):
    if number1 != number2:
        print(max(number1, number2))
compare_2numbers_method2(9, 7)


def compare_2numbers_method3(a, b):
    if type(a) == float and type(b) == float:
    #OR if a == float(a) and b == float(b):
        if a != b:
            print("The greater nume is {}".format(max(a, b)))
    else:
        print("This is not number type.")
compare_2numbers_method3(9, 7)


def compare_2numbers_method4(a, b):
    if a > b:
        print(a)
        return a
    elif a < b:
        print(b)
        return b
print("The greater number is " + str(compare_2numbers_method4(100, 200)))

"""============================================================================
2. Write a function for users to input 1 natural number, check and print if it is an odd or even number.
"""
def natural_number(m):
    if isinstance(m, int):
        if m % 2 == 1:
            return "Odd number"
        elif m % 2 == 0:
            return "Even number"
    else:
        return "Not integer"
natural_number(10)

"""============================================================================
3. Write a function to input a number, return True or False if it can be divisible by 3 or not
"""
def divisible_by_3(x):
    if x % 3 == 0:
        print("True")
    else:
        print("False")
divisible_by_3(10)


def divisible_by_3_method2(x):
    if isinstance(x, int):
        if x % 3 == 0:
            print("True")
            return True
        else:
            print("False")
            return False
    else:
        print("False")
        return False
x = divisible_by_3_method2(10)
# A number divisible by 3 having a remainder = 0 shall not be checked further if it is an integer or not.

def divisbile_by_3_method3(x):
    if x % 3 == 0:
        return True
    return False
x = divisible_by_3_method3(10)


def divisbile_by_3_method4(x):
    if x % 3 == 0:
        return True
    return False
divisbile_by_3_method4(10)


def divisbile_by_3_method5(x):
    return x % 3 == 0
divisbile_by_3_method5(10)


def divisbile_by_3_method6():
    x = int(input("Please enter a number: "))
    return x % 3 == 0
divisbile_by_3_method6()


def divisbile_by_3_method7():
    x = input("Please enter a number: ")
    if x.isdigit():
        x = int(x)
        return x % 3 == 0
    else:
        print("Your input is not an integer.")
divisbile_by_3_method7()

"""============================================================================
4. Write a function to input a string value X, check if X is divisible by 3 (use the function in Q3) to show a result of X/3. If X is not divisible by 3, show the X^2 instead.
"""
#----> Correct Method:
def divisibleby3(a):
    return a % 3 == 0
def check_input():
    x = input("Please enter a number divisible by 3: ")
    if x.isdigit():
        x = int(x)
        if divisibleby3(x):
            return (x/3)
        else:
            return (x**2)
    else:
        print("Only natural numbers.")
check_input()


def check_input():
    x =input('Nhap so kiem tra chia het cho 3: ')
    if x.isdigit():
        x = int(x)
        if sochiahetcho3(x):
            return (x/3)
        else:
            return (x**2)
    else:
        print('Chi xu ly so tu nhien')
check_input()


def hw3(x):
    if x % 3 == 0:
        return("True")
    else:
        return("False")
def hw4():
    x = input("Please enter of number divisible by 3: ")
    if x.isdigit():
        print("===== DEBUG 1: {}".format(type(x)))
        x = int(x)
        y = hw3(x)
        print("===== DEBUG 2: {}".format(type(x)))
        if y == "True":
            return (x/3)
        else:
            return (x**2)
    else:
        print("Only integers to be checked.")
hw4()


#------- Method 1:  
def check_input():
    x =input('Nhap so kiem tra chia het cho 3= ')
    if x.isdigit():
#        print("===== DEBUG 1: {}".format(type(x)))
        x = int(x)
        a = sochiahetcho3(x)
#        print("===== DEBUG 2: {}".format(type(x)))
        if (a == "True"):
            return (x/3)
        else:
           return (x**2)
    else:
        print('Chi xu ly so tu nhien')
check_input()

def check_input():
    x =input('Nhap so kiem tra chia het cho 3= ')
    a = sochiahetcho3(x)
    if x.isdigit():
#        print("===== DEBUG 1: {}".format(type(x)))
        x = int(x)
#        print("===== DEBUG 2: {}".format(type(x)))
        if (a == "True"):
            return (x/3)
        else:
           return (x**2)
    else:
        print('Chi xu ly so tu nhien')
check_input()
        

"""============================================================================
5. Write a function to input a string value.
- Print an alert if X is capitalized of not.
- Print an alert if X is capitalized by the first letter or not.
"""
def check_cap_or_low():
    x = input("Please enter: ")
    if x.islower():
        print("All low.")
    elif x.isupper():
        print("All cap.")
    else:
        print("Both cap and low.")
    print("Capitalized first letter of each word: " + x.title())
    print("Capitalized only first letter of first word: " + x.capitalize())
check_cap_or_low()
   

"""============================================================================
6. Write a function input 2 string values: main_str and sub_str,
- Print out an alert if the output of sub_str is in the main_str or not
- If yes, return the first index of the sub_str in the main_str
"""
#------Method 1:
main_str = "Class of Python of DA"
sub_str = "of"
def hw6(main_str, sub_str):
    if sub_str in main_str:
        print("Yes")
        return main_str.find(sub_str)
    else:
        print("None")
x = hw6(main_str, sub_str)

#------Method 2:
main = "IU est très jolie"
sub = "jolie"
def hw6(x, y):
    if y in x:
        print("Yes")
        return x.find(y)
    else:
        print("Nope")
resu = hw6(x = main, y = sub)

#------Method 3:
main_str = "Python for DA for class 20191230"
sub_str = "for"
def hw6(x, y):
    if y in x:
        print("sub_str is in main_str")
        return x.find(y)
    else:
        print("sub_str is not in main_str")
z = hw6(y = sub_str, x = main_str)