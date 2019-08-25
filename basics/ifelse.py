num = int(input("Enter a number : "))
if num > 0:
    print ("{} is a positive number".format(num))
    print()
elif (num < 0):
    print ("{} is a negative number".format(num))
else:
    print ("{} is zero".format(num))
    print()
    # Say Bye
    print ("Bye")


a = 99 if 99 > 0 else -1  # a is 99
a = 99 if 99 > 100 else -1  # a is -1
a = 99 if 99 else -1 # a is 99
a = 99 if 0 else -1 # a is -1

# printing value of a 
print ("The value of a is: " + str(a))
