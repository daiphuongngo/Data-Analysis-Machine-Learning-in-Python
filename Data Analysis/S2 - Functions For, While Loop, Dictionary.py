# -*- coding: utf-8 -*-
"""
Created on Wed Oct 2 17:02:02 2019

@author: Phuong Dai Ngo
"""

"""============================================================================
6.1 Write a function to input a positive integer n. Return a list of squared numbers of those numbers from 1 --> n.
Ex: 
input: 4
output: [1, 4, 9, 16]
"""
number = 4
resu = [number*number for number in range(1, so+1)]
print(resu)
    

def squarelist(number):
    return [i * i for i in range(1, number+1)]


def squarelist(number):
    resu = []
    for i in range(1, number+1):
        resu.append(i*i)
    return resu
resu = squarelist(4)


def square_positive_integer():
    x = input("Enter a positive integer: ")
    if x.isdigit() == False:
        print("Input in not a number.")
        return
    else:
        x = range(1, int(x) + 1)
        lst = []
        for n in x:
            lst.append(n*n)
        print(lst)
        return lst
resu = square_positive_integer()


def square_positive_integer_method2(x):
    rng = range(1, x+1, 1)
    lst = []
    for i in rng:
        print("=" * 20)
        print("Length of current list: {}".format(len(lst)))
        lst.append(i**2)
        print("i = {} | i**2 = {}".format(i, i**2))
        print("Length of current list after append: {}".format(len(lst)))
    return lst
resu = square_positive_integer_method2(5)


def square_positive_integer_method3(x):
    i = 1
    lst = []
    while i <= x:
        lst.append(i**2)
        i += 1
    print(lst)
    return lst
resu = square_positive_integer_method3(5)

#------------
#Xuống hàng & output list
def squarelist(number):
    y = list()
    number = range(number)
    for x in number:
        print((x+1)**2)
        y.append((x+1)**2)
    print(y)
    return
resu = squarelist(4)

"""============================================================================
7. Write a function to input 2 parameters m: current population and n: number of years, to return a population of a country after n years, the population growth rate is 1.8% per year.
"""
def population_growth(citizen, year):
    i = 1
    while i <= year:
        increased_citizen = citizen * 1.8 / 100
        citizen = citizen + increased_citizen
        i += 1
    print(round(resu))
    return round(citizen)
resu = population_growth(10000, 10)


def population_growth_method2(x, y):
    y = range(y)
    for i in y:
        x = x * 1.018
    print(round(x))
    return round(x)
resu = population_growth_method2(10000, 10)


def population_growth_method3(x, y):
    i = 1
    while i <= y: #****
        x = x * 1.018
        i += 1
    print(round(x))
    return round(x, 2) 
resu = population_growth_method3(10000, 10)

def population_growth_method4(x, y):
    i = 0
    while i < y: #****
        x = x * 1.018
        i += 1
    print(round(x))
    return round(x)
resu = population_growth_method4(10000, 10)

"""============================================================================
8. Write a function to input both new and old electricity rates. 
Show the new and old rates, standard paying amount, paying amount for surplus usage, total paying amount.
Standard rate per household: 50 KW at 230 VND/KW
If 50 KW < over standard amount < 100 KW: paying rate = 700 VND/KW
If over standard rate >= 100KW: paying rate = 900 VND/KW
"""
#----------Method 1:
def electricity_bill():
    old_number = int(input("Enter the old number: "))
    new_number = int(input("Enter the new number: "))
    print("The old number: {}".format(old_number))
    print("The new number: {}".format(new_number))
    
    usage = new_number - old_number
    normal_rate = min(usage, 50)
    excess_rate = max(usage, 50) - 50
    print("Normal rate: {}".format(normal_rate))
    print("Excess rate: {}".format(excess_rate))
    
    spendings_normal_rate = normal_rate * 230 # = 11500
    spendings_excess_rate = 0
    if excess_rate >= 100:
        spendings_excess_rate += (excess_rate - 99) * 900 # = 153900
        excess_rate = 99
    if excess_rate > 50:
        spendings_excess_rate += (excess_rate - 50) * 700 # = 34300
        excess_rate = 50
    if excess_rate > 0:
        spendings_excess_rate += excess_rate * 480 # = 24000
    print("Spendings for normal rate: {}".format(spendings_normal_rate))
    print("Spendings for excess rate: {}".format(spendings_excess_rate))
    print("Total spendings: {}".format(spendings_normal_rate + spendings_excess_rate))
electricity_bill()

#---------Method 2:
def electricity_bill():
    while True:
        number = input("Enter the old numer: ")
        try:
            old_number = int(number)
            break;
        except ValueError:
            try:
                old_number = float(number)
                break;
            except ValueError:
                print("You've entered a string, not a number. \n"
                      "Please enter a number.")
    while True:
        number = input("Enter an the new number: ")
        try:
            new_number = int(number)
            break;
        except ValueError:
            try:
                new_number = float(number)
                break;
            except ValueError:
                print("You've entered a string, not a number. \n"
                      "Please enter a number.")

    excess_amount = new_number - old_number
    normal_rate = 0
    excess_rate = 0
    
    if excess_amount <= 50:
        price = excess_amount * 230
        normal_rate = price
    elif excess_amount <= 100:
        price = (50 * 230) + (excess_amount - 50)*400
    elif excess_amount <= 149:
        price = (50 * 230) + (50 * 480) + (d - 100) * 700
    elif excess_amount > 149:
        price = (50 * 230) + (50 * 480) + (49 * 700) + (excess_amount - 149) * 900
    
    if excess_amount > 50:
        normal_rate = 50 * 230
        excess_rate = price - normal_rate
    
    print("The old amount: " + str(old_number))
    print("The new amount: " + str(new_number))
    print("Spendings for normal rate: " + str(normal_rate))
    print("Spendings for excess rate: " + str(excess_rate))
    print("Total spendings: " + str(normal_rate + excess_rate))
electricity_bill()
    

def PowerPrice():
    oldIndex = int(input("Enter the old index: "))
    newIndex = int(input("Enter the new index: "))
    print("The old index: " + str(oldIndex))
    print("The new index: " + str(newIndex))
    if newIndex >= oldIndex:
        price = 0
        consumePower = newIndex - oldIndex
        
        if consumePower <= 50:
            price = consumePower * 230
        elif consumePower <= 100:
            price = (50 * 230) + (consumePower - 50)*480 
        elif consumePower <= 149:
            price = (50 * 230) + (50 + 480) + (consumePower - 100)*700
        elif consumePower > 149:
            price = (50 * 230) + (50 * 480) + (49 * 700) + (consumePower - 149)*900
        print("Total spendings: " + str(price))
PowerPrice()

"""============================================================================
9. Write a function to return the grade level of student.
Given that student has 4 grades: Math (m), Physics (p), Chemisty (c), and English (e).
4 courses' grades will be input and as per grading scheme 100.

"""
#-------Method 1:
def grade():
    print("Enter marks obtained in 4 subjects: ")
    m = int(input("Please enter Math score: "))
    p = int(input("Please enter Physics score: "))
    c = int(input("Please enter Chemistry score: "))
    e = int(input("Please enter English score: "))
    sum = m + p + c + e
    average = sum / 4
    score = [m, p, c, e]
    if max(score) > 100 and min(score) < 0:
        return "Please enter a score within 0-100."
    if 80 <= average <= 100 and m >= 65 and p >= 65 and c >=65 and e >= 65:
        print("Your Grade is A+.")
    elif 65 <= average <= 79 and m >= 50 and p >= 50 and c >= 50 and e >= 50:
        print("Your Grade is A.")
    elif 50 <= average <= 64 and m >= 20 and p >= 20 and c >= 20 and e >= 20:
        print("Your Grade is B+.")
    else:
        print("Your Grade is B.")
grade()

#--------Method 2:
def grade():
    while True:
        number = input("Enter Math score: ")
        try:
            m = float(number)
            if 0 <= m <= 100:
                break
            print("You've entered it <0 or >100. \nEnter Math score again.")
        except ValueError:
            print("You've entered a string, not a number. \nEnter Math score again.")
    
    while True:
        number = input("Enter Physics score:")
        try:
            p = float(number)
            if 0 <= p <= 100:
                break
            print("You've entered it <0 or >100. \nEnter Physics score again.")
        except ValueError:
            print("You've enter a string, not a number. \nEnter Physics score again.")
        
    while True:
        number = input("Enter Chemistry score: ")
        try:
            c = float(number)
            if 0 <= c <= 100:
                break
            print("You've entered it <0 or >100. \nEnter Chemistry score again.")
        except ValueError:
            print("You've entered a string, not a number. \nEnter Chemistry score again.")
    
    while True:
        number = input("Enter English score: ")
        try:
            e = float(number)
            if 0 <= e <= 100:
                break
            print("You've entered it <0 or >100. \nEnter English score again.")
        except ValueError:
            print("You've entered a string, not a number. \nEnter English score again.")

    if (m+p+c+e)/4 >= 80 and m>=65 and p>=65 and c>=65 and e>=65:
        print("Your Grade is A+.")
    elif (m+p+c+e)/4 >= 65 and m>=50 and p>=50 and c>=50 and e>=50:
        print("Your Grade is A.")
    elif (m+p+c+e)/4 >= 50 and t>=20 and p>=20 and c>=20 and e>=20:
        print("Your Grade is B+.")
    else:
        print("Your Grade is B.")
grade()


#-------Method 3:
def grade():
    math = float(input("Enter Math score: "))
    physics = float(input("Enter Physics score: "))
    chemistry = float(input("Enter Chemistry score: "))
    english = float(input("Enter English score: "))
    score = [math,physics,chemistry,english]
    average = round(sum(score)/len(score))
    if max(score) > 100 or min(score) < 0:
        print("Enter a score with 100-point scale.")
    print(score)
    print(average)
    if min(score) >= 65 and average >= 80:
        print("Your Grade is A+.")
    elif min(score) >= 50 and average >= 65:
        print("Your Grade is A.")
    elif min(score) >= 20 and average >= 50:
        print("Your Grade is B+.")
    else:
        print("Your Grade is B.")
rate = grade()
    
"""============================================================================
10. Write a function to input 2 numbers A, B < 2000, return a list of all numbers divisble by 7 but indivisible by 5, staying in the lists of A and B.
"""
#--------Method 1:
def div7_indiv5(a, b):
    list = []
    if a < 2000 and b < 2000:
        while a <= b:
            if a % 7 == 0 and a % 5 != 0:
                list.append(a)
            a += 1
        else: 
            print("List of satisfactory numbers: " + str(list))
    else:
        print("a and b must be < 2000.")
    return list
div7_indiv5(5, 200)

#--------Method 2 (same as Method 1):
def div7_indiv5(a, b):
    list = []
    if a < 2000 and b < 2000:
        while a <= b:
            if a & 7 == 0 and a % 5 != 0:
                list.append(a)
            a += 1
        print(list)
    else:
        print("a and b must be < 2000.")
div7_indiv5(5, 200)

def taolist(a,b):
    list = []
    if a < 2000 and b < 2000:
        while a <= b:
            if a % 7 == 0 and a % 5 != 0:
                list.append(a)
            a += 1
        print(list)
    else:
        print("Chưa hợp lệ! Hai số không nhỏ hơn 2000")
taolist(5,200)

#--------Method 3:
def div7_indiv5(a, b):
    if a < 2000 and b < 2000 and a <= b:
        list = []
        for i in range(a, b+1):
            if i % 7 == 0 and i % 5 != 0:
                list.append(i)
        print(list)
    else:
        print("a and b must be < 2000.")
div7_indiv5(500, 50)

"""============================================================================
11. Write a function to check if input of a letter string is valid or not. A valid string has at least 8 letters, 1 capitalized letter, 1 digit.
"""
#-----------Method 1:
def password_8capnum():
    while True:
        password = input("Enter a password: ")
        if (len(password) >= 8 and (not password.islower()) and (any(char.isdigit() for char in password))): 
            #at least 1 number
            print("Valid password.")
            break
        else:
            print("Invalid password. \nPlease enter again.")
password_8capnum()


#-----------Method 2:
def password_8capnum():
    password = input("Enter a password: ")
    if len(password) < 8:
        print("Invalid password.")
        return None
    i = 0
    test1 = []
    test2 = []
    
    while i < len(password):
        print("DEBUG | i={} | password[i] = {}".format(i, password[i]))
        if password[i].isupper():
            test1.append(password[i])
        if password[i].isdigit():
            test2.append(password[i])
        i += 1
    if len(test1) > 0 and len(test2) > 0:
        print("Valid password")
    else:
        print("Invalid password")
password_8capnum()


"""============================================================================
12. Create a list of positive round numbers < 60,000 with n digits, sum of powered nth is equal to that number.
Ex:
    153 is a number with 3 digits
    and 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
"""
#-------Method 1:
def sum_power(i): # Armstrong number, narcissistic number
    number = i-1 # nho hon so cho truoc
    lst_result = []
    
    while number > 0: # so nguyen duong
        a = number
        n = int(len(str(a))) # so chu so, cung la bac luy thua
        
        number_quantity = []
        power_quantity = []
        
        while a > 0:
            index = a % 10
            a = int(a / 10)
            number_quantity.append(index)
            print(number_quantity)
        
        for num in number_quantity:
            power = num**n
            power_quantity.append(power)
            
        power_sum = sum(power_quantity)
        if power_sum == number:
            lst_result.append(number)
        number -= 1
        
    if not lst_result:
        print("There are no satisfactory numbers.")
    else:
        print("There are " + str(len(lst_result)) + " satisfactory numbers.")
        return lst_result
sum_power(153)


def kiemtraso(i): # Armstrong number, narcissistic number
    sodangxet = i-1 # nho hon so cho truoc
#Cái này là yêu cầu đề bài thôi. Đề yêu cầu lấy số nhỏ hơn số cho trước. 
#Do mình đi từ số lớn về số nhỏ nên bắt đầu là i - 1.
    lst_ketqua = []
    
    while sodangxet > 0: # so nguyen duong
        a = sodangxet
        n = int(len(str(a))) # so chu so, cung la bac luy thua
    
        cacchuso = []
        cacsoluythua = []
        
        while a > 0:
            chuso = a % 10
            a = int(a / 10)
            cacchuso.append(chuso)
#Đoạn này là lấy ra từng chữ số của một số.  
#Ví dụ số 37482 sẽ lấy ra theo thứ tự là 2, 8, 4, 7, 3.
#Tức là 37482 chia 10 dư 2, lấy số 2, rồi lấy phần nguyên sau khi chia 10 là 3748. 
#Tiếp tục 3748 chia 10 dư 8, lấy số 8, rồi lấy phần nguyên sau khi chia 10 là 374. 
#Cứ thế tiếp tục.
        for so in cacchuso:
            soluythua = so**n
            cacsoluythua.append(soluythua)
    
        tongluythua = sum(cacsoluythua)
        if tongluythua == sodangxet:
            lst_ketqua.append(sodangxet)
        sodangxet -= 1
    
    # neu lst_ketqua khong co phan tu nao
    if not lst_ketqua:
        print('Khong co so nao thoa yeu cau.')
    else:
        print('Co ' + str(len(lst_ketqua)) + ' so thoa yeu cau.')
        return lst_ketqua
kiemtraso(153)


#-------Method 2:
def sum_power(i):
    number = i-1
    lst_result = []
    while number > 0:
        n = int(len(str(number)))
        number_quantity = [int(each_number) for each_number in str(number)] #trả về list
        power_sum = 0
        
        for num in number_quantity:
            power_sum += num**n
        
        if power_sum == number:
            lst_result.append(number)
        number -= 1
        
    if not lst_result:
        print("There are no satisfactory numbers.")
    else:
        print("There are " + str(len(lst_result)) + " satisfactory numbers.")
        return lst_result
sum_power(153)


def kiemtraso(i): # Armstrong number, narcissistic number
    sodangxet = i-1 # smaller than the previous one
    lst_ketqua = []
    while sodangxet > 0: # positive round number
        n = int(len(str(sodangxet))) # number of numbers, also a power number
        cacchuso = [int(mỗi_số) for mỗi_số in str(sodangxet)]
        tongluythua = 0 # must set here to avoid errors in the below loop 

        for so in cacchuso:
            tongluythua += so**n
        
        if tongluythua == sodangxet:
            lst_ketqua.append(sodangxet)
        sodangxet -= 1
    
    # if lst_ketqua has no elements
    if not lst_ketqua:
        print('Khong co so nao thoa yeu cau.')
    else:
        print('Co ' + str(len(lst_ketqua)) + ' so thoa yeu cau.')
        return lst_ketqua
kiemtraso(153)


#-------Method 3:
def sum_power():
    list = []
    for number in range(1, 60000):
        i = 0
        calculation = 0
        while i < len(str(number)):
            calculation += int(str(number)[i]) ** len(str(number))
            i += 1
        if number == calculation:
            list.append(number)
    print(len(list))
    return(list)
sum_power()


def kiemtraso():
    list_so = []
    for sodotim in range(1, 60000):
        i = 0
        pheptinh = 0
        while i < len(str(sodotim)):
            pheptinh += int(str(sodotim)[i]) ** len(str(sodotim))
            i +=1
        if sodotim == pheptinh:
            list_so.append(sodotim)
    print(len(list_so))
    return(list_so)
kiemtraso()


#------- Method 4
list = []
for number in range(1, 60000):
    total = 0
    number_str = str(number)
    for i in number_str:
        total += int(i) ** len(number_str)
        if total > number:
            break
    if total == number:
        list.append(number)
print(list)
print(len(list))

lst = []
for so in range(1, 60000):
    total = 0
    so_str = str(so)
    for i in so_str:
        total += int(i) ** len(so_str)
        if total > so:
            break
    if total == so:
        lst.append(so)
print(lst)
print(len(lst))

"""============================================================================    
13. Given 2 dictionaries, write a function to combine those 2 dictionaries, sum up values of the same key.
Ex:
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}
"""
#----------Method 1****
ini_dict = [{'a': 100, 'b': 200, 'c':300}, 
            {'a': 300, 'b': 200, 'd':400}]
# printing initial dictionary 
print ("initial dictionary", str(ini_dict)) 
  
# sum the values with same keys 
result = {} 
for d in ini_dict: 
    for k in d.keys(): 
        result[k] = result.get(k, 0) + d[k]
#d is dict
#Get value of key k --> each key in each d: abc, abd
#Get value of key k, yes then return, no then 0 
#Sum with key of each value of each dict
#loop 1: 0 + a=100 --> a = 100
#loop 2: 0 + b=200 --> b = 200
#loop 3: 0 + c=300 --> c = 300
#loop 4: a=100 + a=300 --> a = 400
#loop 5: ab=200 + b=200 --> b = 400
#loop 6: 0 + d=400 --> d = 400
#        print("Print 1", result[k])
#        print("Print 2", result.get(k, 0))
#        print("Print 3", d[k])
#        print(d[k])   
print("resultant dictionary : ", str(result)) 


#----------Method 2 - REVIEW
def hw13(dict1, dict2):
    result = dict1.copy()
    for x in dict2:
        if x in result:
            result[x] += dict2[x]
#            print(result)
        else:
            result[x] = dict2[x]
#            print(result)
    print(result)
    return result
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
resu = hw13(d1, d2)


#-------Method 3 - REVIEW
def hw13(dict1, dict2):
    from collections import Counter
    result = Counter(dict1) + Counter(dict2)
    print(result)
    return result
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
resu = hw13(d1, d2)


#------- Method 4 - REVIEW
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}
d3.update(dict.fromkeys(d1))
d3.update(dict.fromkeys(d2))
def hw13():
    for x in d3:
        d3[x]= d1.get(x,0) + d2.get(x,0)
    print(d3)
    return d3
hw13()

#OR

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}
d3.update(dict.fromkeys(d1))
d3.update(dict.fromkeys(d2))
for x in d3:
    d3[x]= d1.get(x,0) + d2.get(x,0)
    

#------------Method 5 - REVIEW
import collections 
ini_dict = [{'a': 100, 'b': 200, 'c':300},  
            {'a': 300, 'b': 200, 'd':400}]
  
# printing initial dictionary 
print ("initial dictionary", str(ini_dict)) 
  
# sum the values with same keys 
counter = collections.Counter() 
for d in ini_dict:  
    counter.update(d) 
#    print(counter)
result = dict(counter) 
#print(result)
print("resultant dictionary : ", str(counter))


#------------Method 6 - REVIEW
from operator import itemgetter # ----> Check again
  
# Initialising list of dictionary 
ini_dict = [{'a': 100, 'b': 200, 'c':300}, 
            {'a': 300, 'b': 200, 'd':400}]  
  
# printing initial dictionary 
print ("initial dictionary", str(ini_dict)) 
  
# sum the values with same keys 
result = {} 
for d in ini_dict: 
    for k in d.keys(): 
        result[k] = result.get(k, 0) + d[k] 
print("resultant dictionary : ", str(result)) 

"""============================================================================
14. Write a function to input a number n <= 30, return a dictionary with length = n with each pair has atype (x:x*x)
Ex:
n = 5
output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""
#------- Method 1
def hw14(x): #  add x into ()
    dict = {} # better than d = dict()
    if 0 < x <= 30:
        for i in range(1, x+1):
            dict[i] = x*x # tag i to avoid mistakes
        print(dict)
        return dict # run all and then return
    else:
        print("This number is more than 30.")
        return "This number is more than 30."
resu = hw14(5)
    
#------- Method 2
def hw14(x):
    if 0 < x <= 30:
        dict = {}
        while x > 0:
            dict[x] = x*x
            x -= 1
        print(dict)
        return dict
    else:
        print("Input must be > 0 and <= 30")
resu = hw14(8)

#------- Method 3
def hw14(x):
    if x <= 0 or x > 30:
        print("Output is incorrect!")
        return "Output is incorrect!"
    result = {}
    for i in range(1, x+1):
        result[i] = i*i
    print(result)
    return result
resu = hw14(5)
        