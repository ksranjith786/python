
# List Compreshension
# Python program showing 
# how to take multiple input 
# using List comprehension 
  
# taking two input at a time 
x, y = [int(x) for x in input("Enter two int values (separated by space): ").split()] 
print("First Number is: ", x) 
print("Second Number is: ", y) 
print() 
  
# taking three input at a time 
x, y, z = [float(x) for x in input("Enter three float values (separated by ;): ").split(';')] 
print("First float Number is: ", x) 
print("Second float Number is: ", y) 
print("Third float Number is: ", z) 
print() 
  
# taking two inputs at a time 
x, y = [str(x) for x in input("Enter only two strings (separated by $): ").split('$', 2)] 
print("First string is {} and second string is {}".format(x, y)) 
print()
  
# taking multiple inputs at a time  
x = [int(x) for x in input("Enter multiple int values: ").split()] 
print("Number of list is: ", x)