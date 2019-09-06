list1 = [1,2]
tuple1 = (1)
tuple2 = (1,)
set1 = {1,2}
dict1 = {1:2, 2:3}

if isinstance(list1, list):
    print (str(list1) + " is a list")

if not isinstance(tuple1, tuple):
    print (str(tuple1) + " is not a tuple")

if isinstance(tuple2, tuple):
    print (str(tuple2) + " is a tuple")

if isinstance(dict1, dict):
    print (str(dict1) + " is a dict")



'''
$ python isinstanceof.py
[1, 2] is a list
1 is not a tuple
(1,) is a tuple
{1: 2, 2: 3} is a dict
'''