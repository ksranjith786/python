name=input("Enter your Name: ")

print ("Your are identified as", name) # default a space is being shown after 'as' and name
print ("You are", name, "as provided") # You are Ranjith as provided
print ("You are"+ name + "as provided") # You areRanjithas provided


num = input("Enter a Number: ")
print (type(num)) # Although the input value is 10, It's string not a integer
numint = int(num)
print ("entered number (num) is "+num)
print ("entered number int(num) is "+ str(numint)) # Will thow TypeError;
print ("entered number is (num)", num)
print ("entered number is int(num)", numint) # will print int

print (type(numint)) # Now it's int as it got type casted


var = input() # prompts user without any string
print(var) # prints whatever is entered

'''
Enter your Name: Ranjith
Your are identified as Ranjith
You are Ranjith as provided
Enter a Number: 2121
<class 'str'>
<class 'int'>


'''