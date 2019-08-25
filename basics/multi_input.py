# https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
#input().split(separator, maxsplit)

# taking two inputs at a time 
x, y = input("Enter a two value: ").split() 
print("Number of boys: ", x) 
print("Number of girls: ", y) 
print() 
  
# taking three inputs at a time 
x, y, z = input("Enter a three value: ").split(';', 2) 
print("Total number of students: ", x) 
print("Number of boys is : ", y) 
print("Number of girls is : ", z) 
print() 
  
# taking two inputs at a time 
a, b = input("Enter a two value: ").split() 
print("First number is {} and second number is {}".format(a, b)) 
print() 
  
# taking multiple inputs at a time  
# and type casting using list() function 
x = list(map(int, input("Enter a multiple value: ").split())) 
print("List of students: ", x) 

'''
$ python multi_input.py
Enter a two value: 1s;  pa
Number of boys:  1s;
Number of girls:  pa

Enter a three value: 1;   5; 6
Total number of students:  1
Number of boys is :     5
Number of girls is :   6

Enter a two value: 43        43
First number is 43 and second number is 43
'''