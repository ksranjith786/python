
# print integer and float value 
print("Geeks : % 2d, Portal : % 5.2f" %(1, 05.333))  
  
# print integer value 
print("Total students : % 3d, Boys : % 2d" %(240, 120)) 
  
# print octal value 
print("% 7.3o"% (25)) 
  
# print exponential value 
print("% 10.3E"% (356.08977))


'''
https://www.geeksforgeeks.org/python-output-formatting/

%[flags][width][.precision]type 

Let’s take a look at the placeholders in our example.
The first placeholder “%2d” is used for the first component of our tuple, i.e. the integer 1. The number will be printed with 2 characters. As 1 consists only of one digits, the output is padded with 1 leading blanks.
The second one “%8.2f” is a format description for a float number. Like other placeholders, it is introduced with the % character. This is followed by the total number of digits the string should contain. This number includes the decimal point and all the digits, i.e. before and after the decimal point.
Our float number 05.333 has to be formatted with 5 characters. The decimal part of the number or the precision is set to 2, i.e. the number following the “.” in our placeholder. Finally, the last character “f” of our placeholder stands for “float”.
'''


# using format() method 
print('I love {} for "{}!"'.format('Geeks', 'Geeks')) 
  
# using format() method and refering  
# a position of the object 
print('{0} and {1}'.format('Geeks', 'Portal')) 
  
print('{1} and {0}'.format('Geeks', 'Portal')) 



# combining positional and keyword arguments 
print('Number one portal is {0}, {1}, and {other}.'
     .format('Geeks', 'For', other ='Geeks')) 
  
# using format() method with number  
print("Geeks :{0:2d}, Portal :{1:8.2f}". 
      format(12, 00.546)) 
  
# Changing positional argument 
print("Second argument: {1:3d}, first one: {0:7.2f}". 
      format(47.42, 11)) 
  
print("Geeks: {a:5d},  Portal: {p:8.2f}". 
     format(a = 453, p = 59.058)) 


name = "Ranjith"
print('My name is \t {}'.format(name)) # My name is Ranjith
print("My name is \t {}".format(name)) # My name is Ranjith
print("My name is {}",format(name)) # My name is {} Ranjith

print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))

tab = {'geeks': 4127, 'for': 4098, 'geek': 8637678} 
  
# using format() in dictionary 
print('Geeks: {0[geeks]:d}; For: {0[for]:d}; '
    'Geeks: {0[geek]:d}'.format(tab)) 
  
data = dict(fun ="GeeksForGeeks", adj ="Portal") 
  
# using format() in dictionary 
print("I love {fun} computer {adj}".format(**data)) 



cstr = "I love geeksforgeeks"
    
# Printing the center aligned   
# string with fillchr  
print ("Center aligned string with fillchr: ")  
print (cstr.center(40, '#'))  
  
# Printing the left aligned   
# string with "-" padding   
print ("The left aligned string is : ")  
print (cstr.ljust(40, '-')) 
  
# Printing the right aligned string  
# with "-" padding   
print ("The right aligned string is : ")  
print (cstr.rjust(40, '-')) 


'''
$ python format.py
Geeks :  1, Portal :  5.33
Total students :  240, Boys :  120
    031
 3.561E+02
I love Geeks for "Geeks!"
Geeks and Portal
Portal and Geeks
Number one portal is Geeks, For, and Geeks.
Geeks :12, Portal :    0.55
Second argument:  11, first one:   47.42
Geeks:   453,  Portal:    59.06
My name is       Ranjith
My name is       Ranjith
My name is {} Ranjith
Geeks: 4127; For: 4098; Geeks: 8637678
I love GeeksForGeeks computer Portal
Center aligned string with fillchr:
##########I love geeksforgeeks##########
The left aligned string is :
I love geeksforgeeks--------------------
The right aligned string is :
--------------------I love geeksforgeeks

rk185212@WINRK185212-172 MINGW64 ~/Google Drive/Learning/Git/python/basics (master)
$

rk185212@WINRK185212-172 MINGW64 ~/Google Drive/Learning/Git/python/basics (master)
$ cls
bash: cls: command not found

rk185212@WINRK185212-172 MINGW64 ~/Google Drive/Learning/Git/python/basics (master)
$ python format.py
Geeks :  1, Portal :  5.33
Total students :  240, Boys :  120
    031
 3.561E+02
I love Geeks for "Geeks!"
Geeks and Portal
Portal and Geeks
Number one portal is Geeks, For, and Geeks.
Geeks :12, Portal :    0.55
Second argument:  11, first one:   47.42
Geeks:   453,  Portal:    59.06
My name is       Ranjith
My name is       Ranjith
My name is {} Ranjith
Geeks: 4127; For: 4098; Geeks: 8637678
I love GeeksForGeeks computer Portal
Center aligned string with fillchr:
##########I love geeksforgeeks##########
The left aligned string is :
I love geeksforgeeks--------------------
The right aligned string is :
--------------------I love geeksforgeeks
'''