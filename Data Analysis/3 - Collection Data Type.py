# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:49:36 2019

@author: Phuong Dai Ngo
"""
# %%
"""===========================================================================
LISTS

- List: a collection which is ordered and changeable. Allows duplicate members.
- Access the list items by referring to the index number
- Negative indexing means beginning from the end, -1 refers to the last item, 
-2 refers to the second last item, etc.
"""
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print(thislist[-1])

"""===========================================================================
- You can specify a range of indexes by specifying where to start and where 
to end the range.
- When specifying a range, the return value will be a new list with the 
specified items.
- Specify negative indexes if you want to start the search from the end 
of the list.
"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[-4:-1])

"""===========================================================================
- To change the value of a specific item, refer to the index number.
- You can loop through the list items by using a for loop.
- To determine if a specified item is present in a list use the in keyword.
- To determine how many items a list has, use the len() method.
"""
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

for x in thislist:
    print(x)
print(len(thislist))

if "banana" in thislist:
    print("Yes, 'apple' is in the fruits list")

"""===========================================================================
- To add an item to the end of the list, use the append() method
- To add an item at the specified index, use the insert() method
- Use remove() method to removes the specified item
- Use pop() method removes the specified index
- Use clear() method empties the list
"""
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
thislist.insert(1, "orange")
print(thislist)
thislist.remove("banana")
print(thislist)
thislist.pop()
print(thislist)
thislist.clear()
print(thislist)

"""===========================================================================
- You cannot copy a list simply by typing list2 = list1, because: list2 will 
only be a reference to list1, and changes made in list1 will automatically 
also be made in list2.
- There are several ways to join, or concatenate, two or more lists in Python:
    + Using the + operator.
    + Appending all the items from list2 into list1, one by one.
    + Use the extend() method, which purpose is to add elements from one list 
    to another list
* Search for more list method
"""
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

for x in list2:
    list1.append(x)

list1.extend(list2)

# %%
"""===========================================================================
TUPLES

- A tuple is a collection which is ordered and unchangeable. In Python 
tuples are written with round brackets.
- Tuples are unchangeable, once a tuple is created, you cannot change its 
values, cannot remove items from it.
- You can delete whole tuple.
"""
thistuple = ("apple", "banana", "cherry")
print(thistuple)

"""===========================================================================
* Keyword are the reserved words in Python, used to define the syntax and 
structure of the Python language.
* We cannot use a keyword as a variable name, function name or any other 
identifier.
"""
del thistuple  # use del to delete variable

# %%

"""===========================================================================
SET 

- A set is a collection which is unordered and unindexed.
- You cannot access items in a set by referring to an index, since sets are 
unordered the items has no index.
- You can loop through the set items using a for loop, or ask if a specified 
value is present in a set, by using the in keyword.
"""
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

print("banana" in thisset)

"""===========================================================================
- To add one item to a set use the add() method.
- To add more than one item to a set use the update() method.
- To remove an item in a set, use the remove() method.
"""
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")
thisset.update(["orange", "mango", "grapes"])
thisset.remove("banana")

"""===========================================================================
- Use the union() method that returns a new set containing all items from 
both sets, or the update() method that inserts all the items from one set 
into another
* Search for more set method
"""
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
set1.update(set2)

# %%
"""===========================================================================
DICTIONARY

-A dictionary is a collection which is unordered, changeable and indexed.
- You can access the items of a dictionary by referring to its key name, 
inside square brackets. or use get() method to get value of item.
- You can change the value of a specific item by referring to its key name.
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

x = thisdict["model"]
x = thisdict.get("model")

thisdict["year"] = 2018

"""===========================================================================
- You can loop through a dictionary by using a for loop.
- When looping through a dictionary, the return value are the keys of the 
dictionary, but there are methods to return the values as well.
- Loop through both keys and values, by using the items() function:
"""
for x in thisdict:  # return keys
    print(x)

for x in thisdict:  # return keys
    print(thisdict[x])

for x in thisdict.values():  # return value
    print(x)

for x, y in thisdict.items():
    print(x, y)

"""===========================================================================
- To determine if a specified key is present in a dictionary use the in 
keyword.
- To determine how many items (key-value pairs) a dictionary has, use the 
len() method.
"""
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
if "Ford" in thisdict.values():
    print("Yes")

"""===========================================================================
- Adding an item to the dictionary is done by using a new index key and 
assigning a value to it
- The pop() method removes the item with the specified key name.
- Use del keyword removes the item with the specified key name
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

thisdict.pop("model")
print(thisdict)

del thisdict["year"]
print(thisdict)

# %%
"""===========================================================================
RANGE()

- The range type represents an immutable sequence of numbers and is commonly 
used for looping a specific number of times in for loops
- The range() function returns a sequence of numbers, starting from 0 by 
default, and increments by 1 (by default), and ends at a specified number.
- Syntax: range(start, stop, step)
"""
x = range(10)
x = range(3, 16, 2)
for n in x:
    print(n)
