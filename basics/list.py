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

import string
print (string.ascii_letters)