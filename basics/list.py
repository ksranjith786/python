#   https://www.geeksforgeeks.org/python-a-b-is-not-always-a-a-b/

'''
nums = [int(x) for x in input("Enter a list of numbers : ").split()]
print(nums)

for i in nums:
    print (i, end=" ")

print("\r")

for i in range(0, len(nums)):
    print (nums[i], end=" ")


for c in range('a', 'z'):
    print c
'''

fib=[]
for i in range(10):
    fib.append(i)

print (fib)

import string
print (string.ascii_letters)



list1 = [5, 4, 3, 2, 1] 
list2 = list1 
list1 += [1, 2, 3, 4] 

print(list1) 
print(list2) 


list1 = [5, 4, 3, 2, 1] 
list2 = list1 
list1 = list1 + [1, 2, 3, 4] 

# Contents of list1 are same as above 
# program, but contents of list2 are 
# different. 
print(list1) 
print(list2) 

'''
expression list1 += [1, 2, 3, 4] modifies the list in-place, means it extends the list such that “list1” and “list2” still have the reference to the same list.
expression list1 = list1 + [1, 2, 3, 4] creates a new list and changes “list1” reference to that new list and “list2” still refer to the old list.
'''