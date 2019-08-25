# https://www.geeksforgeeks.org/using-else-conditional-statement-with-for-loop-in-python/

for i in range(1, 4): 
    print(i) 
else:  # Executed because no break in for 
    print("No Break#1")

print()

for i in range(1, 4): 
    print(i) 
    if (i==2): break
else:  # Does not execute, as break in for is reached 
    print("No Break#2") 

print()

for i in range(1, 4): 
    if (i < 0):
        print(i)
    if i > 4:
        break
else:  # Executed because break in for did not reached
    print("Nothing printed")

'''
$ python for.py
1
2
3
No Break#1

1
2

Nothing printed
'''

count = 0
while (count < 1):     
    count = count+1
    print(count) 
    break
else: 
    print("No Break") 

# will print 1;