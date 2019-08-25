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

