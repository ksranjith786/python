print("Hi Ranjith")

print("[\"]Hi Ran\tjith\n")
print()
print('[\']Hi Ran\tjith\n')

print ("Hi", end = "") # char at end can be anything; no spaces
print ("Ranjith")

print ("Hi", end = " ") # char at end can be anything; 1 space
print ("Ranjith")

print ("Hi", end = ";") # char at end can be anything; semi colon
print ("Ranjith")

print ("Hi", end = "\n") # char at end can be anything; new line
print ("Ranjith")

print ("Hi", end = "\t") # char at end can be anything; tab
print ("Ranjith")

print ("Hi", end = "!@#$") # char at end can be anything; some random string
print ("Ranjith")

print(1) 
# Output: 1 
  
# Code 2 : 
print((1)) 
# Output: 1 
  
# Code 3: 
print(1, 2) 
# Output: 1 2 
  
# Code 4: 
print((1, 2)) 
# Output: (1, 2)

print()

'''
The actual syntax of the print() function is
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
Here, objects is the value(s) to be printed.
The sep separator is used between the values. It defaults into a space character.
After all values are printed, end is printed. It defaults into a new line.
The file is the object where the values are printed and its default value is sys.stdout (screen). Here are an example to illustrate this.
'''
print(1,2,3,4)
# Output: 1 2 3 4

print(1,2,3,4,sep='*')
# Output: 1*2*3*4

print(1,2,3,4,sep='#',end='&')
# Output: 1#2#3#4&


# using triple quotes
print('''He said, "What's there?"''')

# escaping single quotes
print('He said, "What\'s there?"')

# escaping double quotes
print("He said, \"What's there?\"")