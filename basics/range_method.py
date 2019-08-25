# https://www.geeksforgeeks.org/python-range-method/

# range() is commonly used in for looping hence, knowledge of same is key aspect when dealing with any kind of Python code.
# Syntax : range(start, stop, step)
'''
Parameters : 
start : Element from which sequence constructed has to start. (default:0)
stop : Element number at which numbers in sequence have to end (exclusive).
step : Can be +ve or -ve number, denoting the elements need to be skipped during filling of list. (default:1)

Returns : The list using the formula :
list[n] = start + step*n (for both positive and negative step) where, n >=0 and list[n] = 0 and list[n] > stop (for negative step)

Returns ValueError if step is 0. Value constraint is checked in case of step, failing to meet returns empty sequence, else returns sequence according to formula.
'''

list1 = list(range(10))
print (list1)
list1 = list(range(5,10))
print (list1)
list1 = list(range(5,10,1))
print (list1)
list1 = list(range(5,10,-1)) # []
print (list1)
list1 = list(range(5,-5,-1))
print (list1)
list1 = list(range(-9,-5,1))
print (list1)
list1 = list(range(-9,-5,-1)) # []
print (list1)
list1 = list(range(0,10,2))
print (list1)
list1 = list(range(0,10,0)) # ValueError: range() arg 3 must not be zero
print (list1)

'''
$ python range.py
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[5, 6, 7, 8, 9]
[5, 6, 7, 8, 9]
[]
[5, 4, 3, 2, 1, 0, -1, -2, -3, -4]
[-9, -8, -7, -6]
[]
[0, 2, 4, 6, 8]
Traceback (most recent call last):
  File "range.py", line 33, in <module>
    list1 = list(range(0,10,0)) # ValueError: range() arg 3 must not be zero
ValueError: range() arg 3 must not be zero
'''