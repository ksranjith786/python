# Create a new dictionary 
d = dict() # or d = {} 

# Add a key - value pairs to dictionary 
d['xyz'] = 123
d['abc'] = 345

# print the whole dictionary 
print (d )

# print only the keys 
print (d.keys() )

# print only values 
print (d.values() )

# iterate over dictionary 
for i in d : 
	print ("%s %d" %(i, d[i]) )

# another method of iteration 
for index, key in enumerate(d): 
	print (index, key, d[key] )

# check if key exist 
print ('xyz' in d )

# delete the key-value pair 
del d['xyz'] 

# check again 
print ("xyz" in d )

for key, value in d.items(): 
    print(key, value)

prices = {"beer": 2, "fish": 5, "apple": 1}
float_prices = {key:float(value) for key, value in prices.items()}
print(float_prices)

'''
$ python dict.py
{'xyz': 123, 'abc': 345}
dict_keys(['xyz', 'abc'])
dict_values([123, 345])
xyz 123
abc 345
0 xyz 123
1 abc 345
True
False
abc 345
{'beer': 2.0, 'fish': 5.0, 'apple': 1.0}
'''