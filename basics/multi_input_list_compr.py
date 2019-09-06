
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

'''
$ python multi_input_list_compr.py
Enter two int values (separated by space): 12 3
First Number is:  12
Second Number is:  3

Enter three float values (separated by ;): 1.234;45.32;12
First float Number is:  1.234
Second float Number is:  45.32
Third float Number is:  12.0

Enter only two strings (separated by $): A4t$%^&
First string is A4t and second string is %^&

Enter multiple int values: 66 77 3 244 21 7 29
Number of list is:  [66, 77, 3, 244, 21, 7, 29]
'''