# https://www.geeksforgeeks.org/python-set-5-exception-handling/
# https://www.geeksforgeeks.org/multiple-exception-handling-in-python/
# https://www.geeksforgeeks.org/python-raising-an-exception-to-another-exception/
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


# Python code to illustrate 
# working of try() 
def divide(x, y): 
	try: 
		# Floor Division : Gives only Fractional Part as Answer 
		result = x // y 
		print("Yeah ! Your answer is :", result) 
	except ZeroDivisionError: 
		print("Sorry ! You are dividing by zero ") 

# Look at parameters and note the working of Program 
divide(3, 2)
divide(3, 0)



# Program to depict else clause with try-except 

# Function which returns a/b 
def AbyB(a , b): 
	try: 
		c = ((a+b) / (a-b)) 
	except ZeroDivisionError: 
		print ("a/b result in 0")
	else: 
		print (c)

# Driver program to test above function 
AbyB(2.0, 3.0) 
AbyB(3.0, 3.0) 


# Program to depict Raising Exception 

try: 
	raise NameError("Hi there") # Raise Error 
except NameError: 
	print ("An exception")
	raise # To determine whether the exception was raised or not 

print ("Bye") # This wont execute as exception rose