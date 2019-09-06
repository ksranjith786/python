# https://www.geeksforgeeks.org/python-list-comprehension-and-slicing/

evens = [i for i in (0, 100)]
print (evens)

evens = [i for i in [0, 100]]
print (evens)

evens = [i for i in range(0, 100)]
print (evens)

evens = [i for i in range(0, 100) if i % 2 == 0]
print (evens)

print()


'''
A list comprehension generally consist of these parts :
   Output expression, 
   input sequence, 
   a variable representing member of input sequence and
   an optional predicate part. 

For example :

lst  =  [x ** 2  for x in range (1, 11)   if  x % 2 == 1] 

here, x ** 2 is output expression, 
      range (1, 11)  is input sequence, 
      x is variable and   
      if x % 2 == 1 is predicate part.
'''

print()

pow2 = [2 ** x for x in range(10)]
# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(pow2)

# This code is equivalent to
pow2 = []
for x in range(10):
   pow2.append(2 ** x)

# A list comprehension can optionally contain more for or if statements. An optional if statement can filter out items for the new list. Here are some examples.
'''
>>> pow2 = [2 ** x for x in range(10) if x > 5]
>>> pow2
[64, 128, 256, 512]
>>> odd = [x for x in range(20) if x % 2 == 1]
>>> odd
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> 
'''
prglist = [x+y for x in ['Python ','C '] for y in ['Language','Programming']]
print (prglist) # ['Python Language', 'Python Programming', 'C Language', 'C Programming']


# below list contains square of all odd numbers from 
# range 1 to 10
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1] 
print (odd_square )
  
# for understanding, above generation is same as, 
odd_square = [] 
for x in range(1, 11): 
    if x % 2 == 1: 
        odd_square.append(x**2) 
print (odd_square)

# below list contains power of 2 from 1 to 8 
power_of_2 = [2 ** x for x in range(1, 9)] 
print (power_of_2)

print()

# initializing list   
test_list = [1, 4, 5, 6, 7, 3] 
  
# printing original list 
print ("The original list is : " + str(test_list)) 
  
# using list comprehension 
# to assign variables from list element 
var1, var2, var3 = [test_list[i] for i in (1, 3, 5)] 
  
# printing result 
print ("The variables are : " +  str(var1) + 
                           " " + str(var2) +
                            " " + str(var3))


# list for lowering the characters 
print ([x.lower() for x in ["A","B","C"]])
  
# list which extracts number 
string = "my phone number is : 11122 !!"
  
print("\nExtracted digits") 
numbers = [x for x in string if x.isdigit()] 
print (numbers)
  
# A list of list for multiplication table 
a = 5
table = [[a, b, a * b] for b in range(1, 11)] 
  
print("\nMultiplication Table") 
for i in table: 
    print (i)


'''
$ python list_comprehension.py
[0, 25, 50, 100]
[0, 100]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]


[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
['Python Language', 'Python Programming', 'C Language', 'C Programming']
[1, 9, 25, 49, 81]
[1, 9, 25, 49, 81]
[2, 4, 8, 16, 32, 64, 128, 256]

The original list is : [1, 4, 5, 6, 7, 3]
The variables are : 4 6 3
['a', 'b', 'c']

Extracted digits
['1', '1', '1', '2', '2']

Multiplication Table
[5, 1, 5]
[5, 2, 10]
[5, 3, 15]
[5, 4, 20]
[5, 5, 25]
[5, 6, 30]
[5, 7, 35]
[5, 8, 40]
[5, 9, 45]
[5, 10, 50]
'''