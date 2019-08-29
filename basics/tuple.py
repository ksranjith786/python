num = ()
print (len(num))

num = ("ab") # Treats as a single string instead of tuple
print (num)

num = ("ab",) # Extra , makes the single string as tuple
print (num)

num = 10,20,30
print (num)
print (num[0])
# print (num[3]) # Causes the program to terminate with exception as the tuple index out of range;

# Try using try-except block, which will not terminate
try:
    print (num[3])
except IndexError:
    print ("Exception Caught: index Out of range")

print(num.index(20))

# print(dir(num))

print ("Bye")




'''
$ python tuple.py
0
ab
('ab',)
(10, 20, 30)
10
Exception Caught: index Out of range
1
'''

'''
0
ab
('ab',)
(1, 2, 3)
1
Traceback (most recent call last):
  File "tuple.py", line 13, in <module>
    print (num[3])
IndexError: tuple index out of range
'''

'''
$ python tuple.py
0
ab
('ab',)
(10, 20, 30)
10
Exception Caught: index Out of range
Traceback (most recent call last):
  File "tuple.py", line 21, in <module>
    print(num.index(2))
ValueError: tuple.index(x): x not in tuple
'''