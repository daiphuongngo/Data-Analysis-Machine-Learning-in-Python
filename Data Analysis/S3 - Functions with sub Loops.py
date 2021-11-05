# -*- coding: utf-8 -*-
"""
Created on Wed Oct 9 15:00:40 2019

@author: Phuong Dai ngo
"""

"""============================================================================
15. Write a function to calculate the frequency of word (with space " ") from input. Print the output after sorting the alphbets.
- Input: 
New to Python or choosing between Python 2 and Python 3? Read Python 2 or 
Python 3.
- Output: 2:2 , 3.:1 , 3?:1 , New:1 , Python:5 , Read:1 , and:1 , between:1 ,
 choosing:1 , or:2 , to:1
"""
#-------Method 1

def bai15_method1():
    word = input("Please enter: ")
    wordlist = word.split()
    wordfreq = []
    for w in wordlist:
        wordfreq.append(wordlist.count(w))
#        print("String\n" + word +"\n")
#        print("List\n" + str(wordlist) + "\n")
#        print("Frequencies\n" + str(wordfreq) + "\n")
#        print("Pairs\n" + str(list(zip(wordlist, wordfreq))))
        print(wordfreq)
#        continue
bai15_method1()


#-------Method 2
def frequency(txt):
    if len(txt) > 0:
        list_txt = txt.split()
        list_txt.count("2")
        
        set_text = set(list_txt)
        
        dict_txt = {}
        for word in set_text:
            print("Key: {} | Value: {}".format(word, list_txt.count(word)))
            dict_txt[word] = list_txt.count(word)
            
        for i in sorted(dict_txt):
            print({i: dict_txt[i]})
        
        list_result = [key,doct_txt[key]) for key in dict_txt]
        list_result.sort()
        print(list_result)
frequency(wordlist)

wordlist = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
def tansuat(txt):
    if len(txt) > 0:
        #tạo list chứa từng từ
        list_txt = txt.split()
        list_txt.count("2")
        
        #tạo set chứa giá trị không duplicate
        set_txt = set(list_txt)
        
        #tạo dictionary chứa tần suất các từ
        dic_txt = {}
        for tu in set_txt:
            print("Key: {} | Value: {}".format(tu, list_txt.count(tu)))
            dic_txt[tu] = list_txt.count(tu)    
            
        #in ra dictionary được sắp xếp tăng dần
        #cách xếp thứ tự 1
        for i in sorted(dic_txt): 
            print({i: dic_txt[i]})
        #cách xếp thứ tự 2
        list_kq = [(key,dic_txt[key]) for key in dic_txt]
        list_kq.sort()
        print (list_kq)
        
tansuat(wordlist)

#-------Method 3_1 ---- ***
def hw15_method3_1():
    wordlist = input("Enter a string: ")
    wordsfreq = {}
    for w in wordlist.split():
        wordsfreq[w] = wordsfreq.get(w,0) + 1 #add into 
    for key in sorted(wordsfreq):
        print("{}:{}".format(key,wordsfreq[key]))
hw15_method3_1()


#-------Method 3_2
wordlist = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
def bai15_method2(wordlist):
    wordsfreq = {}
    for w in wordlist.split():
        print("Add key {} | value cu {} | value moi {}".format(w, wordsfreq.get(w,0), wordsfreq.get(w,0)+1))
        key = w
        value_cu = wordsfreq.get(w, 0)
        value_moi = value_cu + 1
        wordsfreq[key] = value_moi
        
        wordsfreq[w] = wordsfreq.get(w,0) + 1
        
    for key in sorted(wordsfreq):
        print("{}:{}".format(key,wordsfreq[key]))

bai15_method2(wordlist)

wordlist = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
def hw15_method3_2(wordlist):
    wordsfreq = {}
    for w in wordlist.split():
        print("Add key {} | old value {} | new value {}".format(w, wordsfreq.get(w,0), wordsfreq.get(w,0)+1))
        key = w
        old_value = wordsfreq.get(w, 0)
        new_value = old_value + 1
        wordsfreq[key] = new_value
        wordsfreq[w] = wordsfreq.get(w,0) + 1
    
    for key in sorted(wordsfreq):
        print("{}:{}".format(key,wordsfreq[key]))
hw15_method3_2(wordlist)
    
"""============================================================================
16. Write a module triangle with functions:
- Check the triangle type
- Calculate triangle's perimeter
- Calculate the triangle's area
Input 3 lengths of the triangle
"""

#from tutorial.bt import triangle as tri
from Package1 import triangle as tri
def triangle(x,y,z):
    if x+y <= z or x+z <=y or y+z <= x:
        print("This is not a triange.")
    else:
        triangle_type = tri.type(x,y,z)
        triangle_perimeter = tri.perimeter(x,y,z)
        triangle_area = tri.area(x,y,z)
        print("This is a {}.".format(triangle_type))
        print("Triangle perimeter = {}".format(triangle_perimeter))
        print("Triangle area = {}.".format(triangle_area))
triangle(4,3,5)


#-----Vietnamese
from tutorial.bt import triangle as tri
from Package1 import triangle as tri
def tamgiac(x,y,z):
    if x+y <= z or x+z <= y or y+z <= x:
        print('Day khong phai la tam giac.')
    else:
        ltg = tri.loaitamgiac(x,y,z)
        cvtg = tri.chuvitamgiac(x,y,z)
        dttg = tri.dientichtamgiac(x,y,z)
        print('Day la {}.'.format(ltg))
        print('Chu vi tam giac = {}'.format(cvtg))
        print('Dien tich tam giac = {}'.format(dttg))    
tamgiac(4,3,5)

"""============================================================================
17. Build a function to return a matrix with size N*N
Input: N = 3
Ouput = [[1,0,0],[0,1,0],[0,0,1]]
"""
#=======Method 0
import numpy as np
a = np.eye(3,3)
print(a)          
print(type(a))

import numpy as np
def bai17(n):
    a = np.eye(n,n)
    print(a)
kq = bai17(3)   

#------- Method 1
def build_matrix(n):
    m = []
    while len(m) < n: # hang
        print("="*40)
        print("len(m) = {}".format(len(m)))
        print(m)
        m.append([])
        print("len(m) append = {}". format(len(m)))
        print(m)
        while len(m[-1]) < n: # cot
            print("-"*40)
            print("len(m[-1]) = {}".format(len(m[-1])))
            print(m)
            m[-1].append(0)
            print("len([m[-1]) append = {}".format(len(m[-1])))
            print(m)
    for i in range(n):
        m[i][i] = 1
    return m
build_matrix(3)
    

def build_matrix(n):
    m = []
    while len(m) < n: # hang
        print("="*40)
        print("len(m) = {}".format(len(m)))
        print("m1 is ", m)
        m.append([])
        print("len(m) append = {}". format(len(m)))
        print("m2 is ", m)
        while len(m[-1]) < n: # cot
            print("-"*40)
            print("len(m[-1]) = {}".format(len(m[-1])))
            print("m3 is ", m)
            m[-1].append(0)
            print("len([m[-1]) append = {}".format(len(m[-1])))
            print("m4 is ", m, "\n")
    for i in range(n):
        m[i][i] = 1
        print("m[i] is ", m[i])
        print("[i] is ", [i])
        print("m[i][i] is ", m[i][i], "\n")
    return m
build_matrix(3)


#=========Method 2    
def build_matrix(n):
    matrix = []
    for i in range(n):
        print("===== Matrix before: {}".format(matrix))
        mtx = []
        for j in range(n):
            if i == j:
                mtx.append(1)
            else:
                mtx.append(0)
            print("======= mtx | {}".format(mtx))
        matrix.append(mtx)
        print("======= Matrix after: {}".format(matrix))
#    print(matrix)
    return matrix

mt = build_matrix(3)

for line in mt:
#    print(line)
    print(line[:-1]) # chạy từ đầu và ko bao gồm index sau dấu :
    for number in line[:-1]:
        print("{}, ".format(number), end="") # end là ko xuống dòng
        print("|")
#    print(line[2])
    print(line[-1]) # line này vẫn là line đầu tiên trên cùng trong mt
#    print(line[0])
#    print(line[1])
    


#%% 17.1
"""============================================================================
17.1 Print a matrix of dimension N*N.
Ex Input: N = 3
Output:
1,0,0
0,1,0
0,0,1

Python String join() Method
Definition and Usage
The join() method takes all items in an iterable and joins them into one string.
A string must be specified as the separator.

Syntax
string.join(iterable)
Parameter Values
Parameter: iterable	required
Description: Any iterable object where all the returned values are strings.

Python map() Function
Definition and Usage
The map() function executes a specified function for each item in a iterable. 
The item is sent to the function as a parameter.

Syntax
map(function, iterables)
Parameter Values
function	: Required. The function to execute for each item.
iterable	: Required. A sequence, collection or an iterator object. You can send as many 
    iterables as you like, just make sure the function has one parameter for each iterable.
"""
#------- Method 1
for line in mt:
    for number in line[:-1]:
        print("{}, ".format(number), end="")
    print(line[-1])
    
#------- Method 2
for l in mt:
    print(", ".join(map(str, l)))

for line in mt:
    print(", ".join(map(str, line)))    
         
"""============================================================================
18. Build a module mymath.py with functions:
- Print the most frequent values in a list of numbers, return its value as well. (use mode() in statistics)
Ex: Input:[1,2,5,7,3,7,7,5,8,5]
Output: 5, 7

Check if it is a square number, a prime number, a factorial

Create a file named main.py to call the function from the module mymath
"""
test_list = [1,2,5,7,3,7,7,5,8,5]
print("Original list: " + str(test_list))

def bai18():
    max = 0
    res = test_list[0]
    for i in test_list:
        freq = test_list.count(i)
        if freq > max :
            max = freq
            res = i
            print("Most frequent numbers are: ", res)
kq = bai18()


from statistics import mode
test_list = [1,2,5,7,3,7,7,5,8,5]
print("Original list: " + str(test_list))
res = mode(test_list)
print("Most frequent numbers are: ", str(res))

    
def isSquareNumber(num):
    if number <= 0:
        return False
    else:
        isSquareNum = False
        for i in range(1, number + 1):
            if i * i == number:
                isSquareNum = True
                break
        
        if isSquareNum == True:
            return True
        else:
            return False
#Chúng ta định nghĩa hàm def isSquareNumber(num)và còn nội dung chương trình thì 
#giữ nguyên nguyên như bài trước. Bây giờ, ta sẽ nhập giá trị và gọi hàm để kiểm 
#tra một số có phải là số chính phương không nhé.


#-------Method 2:
number = int(input("Nhap vao mot so nguyen:"))

result = isSquareNumber(number)

if result == True:
    print( number, " la so chinh phuong")
else:

    print(number, " khong phai la so chinh phuong")

def giaithua1(n):
    if n == 1:
        return 1
    else:
        return n * giaithua1(n - 1)

def giaithua2(n):
    fact = [1]
    dem = 0
    for i in range(2, n + 1):
        fact.append(fact[dem] * i)
        dem += 1
    return fact[dem - 1]

if __name__ == '__main__':
    n = int(input('Nhap n = '))
    print("Cach de quy:")
    print(giaithua1(n))
    print("Cach quy hoach dong:")
    print(giaithua2(n + 1))

#change the value for a different result

num = 7
# To take input from the user
#num = int(input("Enter a number: "))
factorial = 1
# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


"""============================================================================
19. Print 10 files with structure like:
The 1st row is file id (id = 1,2..10), 
Next rows are n rows of "Hello world!" with n = id.
Ex: 
file 1:
id 1
Hello world!
file 2:
id 2
Hello world!
Hello world!
file 3 :
id 3
Hello world!
Hello world!
Hello world!
"""
#============ Official
import glob
f = glob.glob("/Users/phuongdaingo/Documents/Python/PythonFrankie/Package1/id*.txt")
def file_id():
    f_open = open(f, "w")
    i = 1
    number = 1
    txt = "id = "
    content = "Hello world!" + "\n"
    for file in f_open:
        for i in range(1):
            f_open.wrtie(txt)
            print(number)
            num = str(number)
            f_open.write(num)
            f_open.write("\n")
            f_open.write(content*(i+1))
        f_open.close()
file_id()



import glob
f = glob.glob("/Users/phuongdaingo/Documents/Python/PythonFrankie/Package1/id*.txt")
def file_id():
    resu = open(f, "w+")
    i = 1
    number = 1
    txt = "id = "
    content = "Hello world!" + "\n"
    for file in resu:
        for i in range(1, 10):
            resu.write(txt)
            print(number)
            num = str(number)
            file.write(num)
            file.write("\n")
            file.write(content*i)
            i +=1
    resu.close()
file_id()


#============ Right but not Official:
s1 = "/Users/phuongdaingo/Documents/Python/PythonFrankie/Package1/id1"
s2 = "/Users/phuongdaingo/Documents/Python/PythonFrankie/Package1/id2"
s3 = "/Users/phuongdaingo/Documents/Python/PythonFrankie/Package1/id3"
s4 = "/Users/phuongdaingo/Documents/Python/PythonFrankie/Package1/id4"
s5 = "/Users/phuongdaingo/Documents/Python/PythonFrankie/Package1/id5"
s6 = "/Users/phuongdaingo/Documents/Python/PythonFrankie/Package1/id6"
s7 = "/Users/phuongdaingo/Documents/Python/PythonFrankie/Package1/id7"
s8 = "/Users/phuongdaingo/Documents/Python/PythonFrankie/Package1/id8"
s9 = "/Users/phuongdaingo/Documents/Python/PythonFrankie/Package1/id9"
s10 = "/Users/phuongdaingo/Documents/Python/PythonFrankie/Package1/id10"

def file_id():
    f1 = open(s1, "w")
    f2 = open(s2, "w")
    f3 = open(s3, "w")
    f4 = open(s4, "w")
    f5 = open(s5, "w")
    f6 = open(s6, "w")
    f7 = open(s7, "w")
    f8 = open(s8, "w")
    f9 = open(s9, "w")
    f10 = open(s10, "w")
    i = 1
    number = 1
    txt = "id = "
    content = "Hello world!" + "\n"
    for i in range(1):
        f1.write(txt)
        print(number)
        num = str(number)
        f1.write(num)
        f1.write("\n")
        f1.write(content*(i+1))
        
        i += 1
        number += 1
        print(number)
        f2.write(txt)
        num = str(number)
        f2.write(num)
        f2.write("\n")
        f2.write(content*(i+1))
        
        i += 1
        number += 1
        print(number)
        f3.write(txt)
        num = str(number)
        f3.write(num)
        f3.write("\n")
        f3.write(content*(i+1))
        
        i += 1
        number += 1
        print(number)
        f4.write(txt)
        num = str(number)
        f4.write(num)
        f4.write("\n")
        f4.write(content*(i+1))
        
        i += 1
        number += 1
        print(number)
        f5.write(txt)
        num = str(number)
        f5.write(num)
        f5.write("\n")
        f5.write(content*(i+1))
        
        i += 1
        number += 1
        print(number)
        f6.write(txt)
        num = str(number)
        f6.write(num)
        f6.write("\n")
        f6.write(content*(i+1))
        
        i += 1
        number += 1
        print(number)
        f7.write(txt)
        num = str(number)
        f7.write(num)
        f7.write("\n")
        f7.write(content*(i+1))
        
        i += 1
        number += 1
        print(number)
        f8.write(txt)
        num = str(number)
        f8.write(num)
        f8.write("\n")
        f8.write(content*(i+1))
        
        i += 1
        number += 1
        print(number)
        f9.write(txt)
        num = str(number)
        f9.write(num)
        f9.write("\n")
        f9.write(content*(i+1))
        
        i += 1
        number += 1
        print(number)
        f10.write(txt)
        num = str(number)
        f10.write(num)
        f10.write("\n")
        f10.write(content*(i+1))
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f7.close()
    f8.close()
    f9.close()
    f10.close()
file_id()


#import hello_world.py as hw
def file_id():
    txt = "Hello world!\n"
    i = 1
    for i in range(1, 11):
        print("id ", int(i))
        print(txt*i)
    i += 1
file_id()

s1 = "/Users/phuongdaingo/Documents/Python/PythonFrankie/Package1/id1"
def file_id1(s1):
    file = open(s1)
    id_file = file.readline()
    txt = "Hello World!"
    for line in file:
        id_file = line.split("=")
        if id_file[0] == "id":
            print(id_file[0], " ", id_file[1])

    file.close()
#    print(txt*int(id_file[1]))
    print(int(id_file[1]))
file_id1(s1)

s = "/Users/phuongdaingo/Documents/Python/PythonFrankie/Package1/id1"
def file_id(s):
    file = open(s)
    id_file = file.readline()
    txt = file.readline()
    for line in file:
        arr = line.split("=")
        if arr[0] == "id":
            print("id = ", int(arr[1]))
        x = int(arr[0])
        print(txt*x)
    file.close()
    print("id = ", int(arr[1]))
    print(txt*x)
file_id(s)


"""============================================================================
20.
Write a function to receive the file transaction.txt with the 1st row as account id, 2nd row as account number, 3rd row as remaining balance, next rows as below:
- With D,100: deposit $100 into the bank.
- With W,100: withdraw $100 from the bank.
The function returns the last remaining balance of the account.
Ex: 
input:
Id1
Tk01
400
D,100
W,200
-> output: 300
"""
#------- Method 1
path = "/Users/phuongdaingo/Documents/Python/PythonFrankie//Package1/transaction"
def check_account_balance(path):
    file = open(path)
    account_id = file.readline()
    account_number = file.readline()
    account_balance = int(file.readline())
    for line in file:
        arr = line.split(",")
        if arr[0] == "D":
            account_balance += int(arr[1])
        elif arr[0] == "W":
            account_balance -= int(arr[1])
    file.close()
    print("ID account: {} | Account numner: {} | Account balance: {}".format(
            account_id, account_number, account_balance))
    return account_balance
check_account_balance(path)

#--------_Vietnamese:
path = "/Users/phuongdaingo/Documents/Python/PythonFrankie//Package1/transaction"
def check_account(path):
    file = open(path)
    id_tk = file.readline()
    so_tk = file.readline()
    so_du = int(file.readline())
    for line in file:
        arr = line.split(",")
        if arr[0] == "D":
            so_du += int(arr[1])
        elif arr[0] == "W":
            so_du -= int(arr[1])
    file.close()
    print("Tai khoan ID: {} | SoTK: {} | So du: {}".format(
        id_tk, so_tk, so_du))
    return so_du
check_account(path)
     

#------- Method 2
path = "/Users/phuongdaingo/Documents/Python/PythonFrankie//Package1/transaction"
def check_account_balance(path):
    file = open(path)
    file.readline() #skip account id
    file.readline() #skip account number   
    account_balance = int(file.readline())
    insert = 0;
    withdraw = 0;
    for line in file: #calculate the balance
        data = line.split(",")
        if (data[0] == "D"):
            insert += int(data[1])
        if (data[0] == "W"):
            withdraw += int(data[1])
    file.close()
    account_balance += insert
    account_balance -= withdraw
    return account_balance
check_account_balance(path)


#--------Vietnamese:
path = "/Users/phuongdaingo/Documents/Python/PythonFrankie//Package1/transaction"
def soDuTK(path):
    f = open(path)
    f.readline() #skip id
    f.readline() #skip so TK
    sodu = int(f.readline())
    nop = 0;
    rut = 0;
    for l in f: #tinh so du
        data = l.split(",")
        if(data[0] == 'D'):
            nop += int(data[1])
        if(data[0] == 'W'):
            rut += int(data[1])
    f.close()
    sodu += nop
    sodu -= rut
    return sodu
soDuTK(path)


#------- Method 3
path = "/Users/phuongdaingo/Documents/Python/PythonFrankie//Package1/transaction"
def check_account_balance(path):
    file = open(path, "r")
    row = 1
    for line in file:
        if row == 3:
            account_balance = int(line)
        elif line[0] == "D":
            seperate = line.split(",")
            insert = int(seperate[1])
            account_balance = account_balance + insert
        elif line[0] == "W":
            seperate = line.split(",")
            withdraw = int(seperate[1])
            account_balance = account_balance - withdraw
        row += 1
    print("Account balance: {}".format(account_balance))
check_account_balance(path)
            
#------Vietnamese
duongdan = "/Users/phuongdaingo/Documents/Python/PythonFrankie//Package1/transaction"
def bai20(duongdan):
    t = open(duongdan, 'r')
    dong = 1
    for l in t:
        if dong == 3:
            sodu = int(l)
        elif l[0] == 'D':
            temp = l.split(',')
            sotien = int(temp[1])
            sodu = sodu + sotien
        elif l[0] == 'W':
            temp = l.split(',')
            sotien = int(temp[1])
            sodu = sodu - sotien
        dong += 1
    
    print('So du cuoi cung: {}'.format(sodu))
bai20(duongdan)

    
"""============================================================================
21. File txt with its content as follows: file the many rows, each row has a student name and Python course's grade separated with ",".
Ex:
Liam,10
Simon,9
"""
s = "/Users/phuongdaingo/Documents/Python/PythonFrankie/Package1/diem_hs"
#------- Method 1:
def FindMaxScore(s):
    student_list = []
    file = open(s)
    maximum = 0 
    for line in file: #Find Max
        data = line.split(",")
        score = int(data[1])
        if score > maximum:
            maximum = score
    print("Max score: {}".format(maximum))
    file.close()
    
    file = open(s)
    for line in file:
        data = line.split(",")
        score  = int(data[1])
        if score == maximum:
            student_list.append(data[0])
            print(line)
    file.close()
#    return student_list, maximum
    print("List of students with max score:", "\n", student_list)
result = FindMaxScore(s)

#----Original on Drive:
def FindScoreMax(s):
    list_hs = []
    f = open(s)
    maximum = 0
    for l in f: #Find Max
        data = l.split(",")
        score = int(data[1])
        if(score > maximum):
            maximum = score
    print("Score Max: {}".format(maximum))    
    f.close()
    
    f = open(s)
    for l in f: #Print Name list
        data = l.split(",")
        score = int(data[1])
        if(score == maximum):
            list_hs.append(data[0])
            # print(l)
    f.close()
    return list_hs, maximum
ds, diem = FindScoreMax(s)


s = "/Users/phuongdaingo/Documents/Python/PythonFrankie/Package1/diem_hs"
#------- Method 2:
def FindMaxScore(s):
    file = open(s, "rt")
    student_list = {} #dictionary
    score = []
    list_with_max_score = []
    lst = []
    for line in file:
        data = line.split(",")
        student_list[data[0]] = int(data[1])
        score.append(int(data[1]))
        lst.append(data[0])
    file.close()
    
    for i in student_list:
        if student_list[i] == max(score):
            list_with_max_score.append(i)
#    return result, max(score)
    print("List with max score: ", list_with_max_score)
    print("Max score is ", max(score))
    print("List of students and score: ", student_list)
    print("Dictionary of student names: ", lst)
resu = FindMaxScore(s)


#-----Original on Drive:
def stud_check(students):
    f = open(students,"rt")
    stud = {}
    score = []
    res = []
    for n in f:
        lst = n.split(",")
        stud[lst[0]] = int(lst[1])
        score.append(int(lst[1]))
    f.close()
    
    for i in stud:
        if stud[i] == max(score):
            res.append(i)
    return res, max(score)
ds, diem = stud_check(s)    


"""===========================================================================
22. Find the smallest positive round number N divisible by all numbers in the range 1-20.
"""
#------Method needed to be checked its functions
def gcd(x,y): return y and gcd(y, x % y) or x
def lcm(x,y): return x * y / gcd(x,y)

n = 1
for i in range(1, 21):
     n = int(lcm(n, i))
print(n)


def gcd(x,y): 
    return y and gcd(y, x % y) or x
def lcm(x,y): 
    return x * y / gcd(x,y)
n = 1
for i in range(1, 21):
     n = int(lcm(n, i))
print(n)

#------Method 1:
def least_common_multiple(rng):
    n = 1
    for x in rng: #với mỗi x = 1, run y 20 lần
        for y in rng:
            if (n * y) % x == 0:
                print("n is ", n)
                print("y is ", y)
                print("x is ", x)
                n *= y
                print("n' is ", n, "\n")
                break #dừng cho for / while gần nhất
    return n
result = range(1, 21)
print(least_common_multiple(result))

#n=1, x=1, y=1, break/valid --> n=1*1=1
#n=1, x=2, y=1, invalid
#n=1, x=2, y=2, valid --> n=1*2=2
#n=2, x=3 y=1, invalid
#n=2, x=3, y=2, valid --> n=2*2=4
#n=4, x=3, y=3 valid --> n=4*3=12
#n=12 x=4 y=1 valid --> n=12*1=12
#n=12 x=5 y=1, invalid
#n=12 x=6 y=1 valid --> n=12*6=72

#--------Vietnamese
def cach1_least_common_multiple(rng):
    n = 1
    for x in rng:
        for y in rng:
            if (n * y) % x == 0: 
                n *= y 
                break
    return n

doan = range(1, 21)
print(cach1_least_common_multiple(doan))


#-------Method 2:
a = 0
k = 20
while a < 20:
    print("=" *20)
    for i in range(1,21):
        if k % i == 0:
            a += 1
            print("a is ", a)
            if a == 20:
                print("K is ", k)
                break
        else:
            a = 0
            print("A is", a)
            k += 20
            print("K is ", k)

#i = 1. a = 1. k = 20
#i = 2. a = 1. --> a = 2. k = 20
#i = 3. a = 2. --> a = 0. k = 40
#i = 4. a = 0. --> a = 1. k = 40
#i = 5. a = 1. --> a = 2. k = 40
#i = 6. a = 2. --> a = 0. k = 60

"""============================================================================
23. Write a function to check the string value input by user, rules as Q11. Add another function if invalid, allow user to input again with max of 4 attempts.
"""
def password_max_attempt():
    count = 0
    while count < 4:
        new_account = input("Enter new password: ")
        if (len(new_account) >= 8 and (not new_account.islower()) and (any(char.isdigit() for char in new_account))):
            print("Valid password.")
            break
        else:
            print("Invalid password.")
            count += 1
    print("Max attempt.")
    return
password_max_attempt()

#---------Method 2
def password():
    password = input("Enter a password: ")
    if len(password) < 8:
        print("Invalid password.")
        return False
    
    i = 0
    test1 = []
    test2 = []
    
    while i < len(password):
        print("DEBUG | i = {} | password{i} = {}".format(i, password[i]))
        if password[i].isupper():
            test1.append(password[i])
        if password[i].isdigit():
            test2.append(password[i])
        i += 1
        
    if len(test1) > 0 and len(test2) > 0:
        print("Valid password.")
        return True
    else:
        print("Invalid password.")
        return False
password()

def password_max_attemtp():
    for i in range(1, 4): #OR for i in range(3):
        if password() == True:
            break
    print("Max attempt.")
password_max_attempt()


#---------Vietnamese:
def kiemtrachuoi():
    chuoi = input("Nhập chuỗi: ")
    if len(chuoi) < 8:
        print("Không hợp lệ!")
        return False
    
    i = 0
    test1 = []
    test2 = []
    
    while i < len(chuoi):
        print("DEBUG | i={} | chuoi[i] = {}".format(i, chuoi[i]))
        if chuoi[i].isupper():
            test1.append(chuoi[i])
        if chuoi[i].isdigit():
            test2.append(chuoi[i])
        i += 1
        
    if len(test1) > 0 and len(test2) > 0:
        print("Hợp lệ!")
        return True
    else:
        print("Không hợp lệ!")
        return False
kiemtrachuoi()

def kiemtrachuoi_nangcao():
    for i in range(1, 4):
        if kiemtrachuoi() == True:
            break
    print("Max attempt.")
kiemtrachuoi_nangcao()


#-------Method 3
def bai24():
    for attempt in range(4):
        txt = input('Xin nhap mot chuoi ky tu: ')
        if (len(txt) >=8 and (not txt.islower()) and (any(char.isdigit() for char in txt))): #it nhat mot ky tu so
            print('Chuoi vua nhap hop le.')
            break
        else:
            if 3 - attempt == 0:
                print('Ban da nhap sai 4 lan, ban khong duoc nhap nua.')
            else:
                print('Chuoi vua nhap khong hop le. \n'
                      'Ban con ' + str(3 - attempt) + ' lan nhap lai.')
bai24()

"""============================================================================
24.
Write a function to input date, month, year. Print out:
- Which date?
- Which date of the month?
- How many days in that month?
- Is that month in a leap year?
"""
#-----Method 1:
import datetime
def calendar():
    info_day = int(input("Enter a day: "))
    info_month = int(input("Enter a month: "))
    info_year = int(input("Enter a year: "))
    date = datetime.datetime(info_year, info_month, info_day)
    print(date.strftime("%A"))
    print(date.strftime("%j"))
    print(number_of_day_in_month(date))
    return date

def check_leap_year(n): #k nhất thiết thay n bằng info_year vì 3 def đã liên kết nhau
    if (n % 4 == 0) and (n % 100 == 0):
        return True
    print("This is leap year.")
    if n % 4 == 0 :
        return True
        print("This is leap year.")
    return False
    print("This is not leap year.")
    
def number_of_day_in_month(date): #k nhất thiết thay date bằng ngay vì 3 def đã liên kết nhau
    month = date.month
    year = date.year
    list_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if check_leap_year(year) and (month == 2):
        return 29
    else:
        return list_month[month]
calendar()

#---------Vietnamese
import datetime
def nhap_input():
    info_ngay = int(input("Nhap ngay :"))
    info_thang = int(input("Nhap thang :"))
    info_nam = int(input("Nhap nam :"))
    ngay = datetime.datetime(info_nam, info_thang, info_ngay)
    print(ngay.strftime("%A"))
    print(ngay.strftime("%j"))
    print(so_ngay_cua_thang(ngay))
    return ngay

def check_leapyear(n):
    if (n % 4 == 0) and (n % 100 == 0):
        return True
    print("This is leap year.")
    if n % 4 == 0 :
        return True
        print("This is leap year.")
    return False
    print("This is not leap year.")

def so_ngay_cua_thang (date):
    thang = date.month
    nam = date.year
    list_thang = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if check_leapyear(nam) and (thang == 2):
        return 29
    else:
        return list_thang[thang]
nhap_input()


#------------DRAFT
#-----Method 2:
from datetime import datetime
def bai25():
    date = str(input("Enter the date in mm/dd//yyyy format: "))
    month,day,year = date.split("/")              
    print(date.strftime("%A"))
    print(date.year)
    print(date.strftime("%j"))
    print(date.strftime("%-d"))
    m = int(month)
    d = int(day)
    y = int(year)
    if y%400 == 0 or y%4 == 0 and y%100 != 0:
        print("This is a Leap Year")
        return
    else:
        print("This is not a Leap Year")
        return
kq = bai25()


from datetime import datetime
def bai25():
    date = str(input("Enter the date in mm/dd//yyyy format: "))
    month,day,year = date.split("/")
#    monthvalidity = monthcheck(int(month))
#    dayvalidity = daycheck(int(month),int(day))
#    yearvalidity = yearcheck(year)                
    print(date.strftime("%A"))
    print(date.year)
    print(date.strftime("%j"))
    print(date.strftime("%-d"))
    m = int(month)
    d = int(day)
    y = int(year)
    if y%400 == 0 or y%4 == 0 and y%100 != 0:
        print("This is a Leap Year")
        return
    else:
        print("This is not a Leap Year")
        return

kq = bai25()

def main(): 
date = str(input("Enter the date in mm/dd/yyyy format: ")) 
## Input date in the given format. 
month,day,year = date.split("/") 
## split the date into 3 separate variables. 
monthvalidity = monthcheck(int(month)) 
dayvalidity = daycheck(int(month),int(day)) 
yearvalidity = yearcheck(year) 
if monthvalidity == True and dayvalidity == True and yearvalidity == True: 
## check if all 3 variables are valid or True 
    print("The date {0} is valid.".format(date)) 
else: 
    print("The date {0} is invalid.".format(date)) main()


def monthcheck(month):
        if month > 0 and month <= 12: ## If month is between 1 and 12, return True.
            return True
        else:
            return False

def daycheck(month,day):
    monthlist1 = [1,3,5,7,8,10,12] ## monthlist for months with 31 days.
    monthlist2 = [4,6,9,11] ## monthlist for months with 30 days.
    monthlist3 = 2 ## month with month with 28 days.

    for mon in monthlist1: ## iterate through monthlist1.
        if month == mon: ## Check if the parameter month equals to any month with 31 days.
            if day >=1 and day <= 31: ## If the parameter day is between 1 and 31, return True.
                return True
            else:
                return False

    for mon in monthlist2: ## iterate through the monthlist with 30 days.
        if month == mon: ## check if the parameter month equals to any month with 30 days.
            if day >= 1 and day <= 30: ## if the parameter day is between 1 and 30,return True.
                return True
            else:
                return False

    if month == monthlist3: ## check if parameter month equals month with 28 days.
        if day >=1 and day <= 28: ## if the parameter day is between 1 and 28,return True.
            return True
        else:
            return False

def yearcheck(year):
    if len(year) >= 1 and len(year) <= 4: ## Check if year has between 1 to 4 numbers and return True.
        return True
    else:
        return False


def main():
    date = str(input("Enter the date in mm/dd/yyyy format: ")) ## Input date in the given format.
    month,day,year = date.split("/") ## split the date into 3 separate variables.
    monthvalidity = monthcheck(int(month)) 
    dayvalidity = daycheck(int(month),int(day))
    yearvalidity = yearcheck(year) 
    m = int(month)
    d = int(day)
    y = int(year)
    date2 = datetime(m, d, y)
    date3 = (date2 - datetime(1, 1, 2020)).days + 1
    if monthvalidity == True and dayvalidity == True and yearvalidity == True: ## check if all 3 variables are valid or True
        print("The date {0} is valid.".format(date))
    else:
        print("The date {0} is invalid.".format(date))
#    date2 = datetime(int(monthvalidity), int(dayvalidity), int(yearvalidity))
    if y%400 == 0 or y%4 == 0 and y%100 != 0:
        print(date2.strftime("%A"))
        print(year)
        print(date2.strftime("%j"))
        print(date2.strftime("%-d"))
        print("This is a Leap Year")
        return   
    else:
        print("This is not a Leap Year")
        return
#    print(datetime.datetime(date2))

#    print(date2 - date(2020, 1, 1))

main()

def main2():
    date = str(input("Enter the date in mm/dd/yyyy format: ")) ## Input date in the given format.
    month,day,year = date.split("/") ## split the date into 3 separate variables.
    m = int(month)
    d = int(day)
    y = int(year)
    date2 = datetime(m, d, y)
    if y%400 == 0 or y%4 == 0 and y%100 != 0:
        print(date2.strftime("%A"))
        print(year)
        print(date2.strftime("%j"))
        print(date2.strftime("%-d"))
        print("This is a Leap Year")
        return   
    else:
        print("This is not a Leap Year")
        return

main2()

x = datetime(2020, 5, 7)
y = datetime(2020, 5, 2)
z = x - y
print(z)

from datetime import datetime
z = (2020, 5, 5)
print(z.strftime("%j"))

from calendar import monthrange
print(monthrange(year,month))
    
