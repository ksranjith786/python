# https://www.geeksforgeeks.org/python-range-function/
# range() is commonly used in for looping hence, knowledge of same is key aspect when dealing with any kind of Python code. Most common use of range() function in Python is to iterate sequence type (List, string etc.. ) with for and while loop.
'''
There are three ways you can call range() :

range(stop) takes one argument.
range(start, stop) takes two arguments.
range(start, stop, step) takes three arguments

range() function only works with the integers i.e. whole numbers.
All argument must be integers. User can not pass a string or float number or any other type in a start, stop and step argument of a range().
All three arguments can be positive or negative.
The step value must not be zero. If a step is zero python raises a ValueError exception.
range() is a type in Python

'''

# printing a number 
for i in range(10): 
    print(i, end =" ") 
print() 
  
# using range for iteration 
l = [10, 20, 30, 40] 
for i in range(len(l)): 
    print(l[i], end =" ") 
print() 
  
# performing sum of natural 
# number 
sum = 0
for i in range(1, 10): 
    sum = sum + i 
print("Sum of first 10 natural number :", sum) 


# printing first 10  
# whole number 
for i in range(10): 
    print(i, end =" ") 
print() 
  
# printing first 20 
# whole number 
for i in range(20): 
    print(i, end = " ")


# printing a natural 
# number upto 20 
for i in range(1, 20): 
    print(i, end =" ") 
print() 
  
# printing a natural 
# number from 5 t0 20 
for i in range(5, 20): 
    print(i, end =" ") 



# using range to print number 
# divisible by 3 
for i in range(0, 30, 3): 
    print(i, end = " ") 
print() 
  
# using range to print number 
# divisible by 5 
for  i in range(0, 50, 5): 
     print(i, end = " ") 


# incremented by 2 
for i in range(2, 25, 2): 
    print(i, end =" ") 
print() 
  
# incremented by 4 
for i in range(0, 30, 4): 
    print(i, end =" ") 
print() 
  
# incremented by 3 
for i in range(15, 25, 3): 
    print(i, end =" ") 


# incremented by -2 
for i in range(25, 2, -2): 
    print(i, end =" ") 
print() 
  
# incremented by -4 
for i in range(30, 1, -4): 
    print(i, end =" ") 
print() 
  
# incremented by -3 
for i in range(25, -6, -3): 
    print(i, end =" ") 

'''
# using a float number 
for i in range(3.3): # exception; ypeError: 'float' object cannot be interpreted as an integer
    print(i) 
'''
print()

print(type(range(3)))
print(range(10))
print(range(10)[2::2])
print(range(10)[2:8:2])
print(range(10)[::])