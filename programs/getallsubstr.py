
str1 = "Ranjith"
str1 = "abdabc"
'''
for i in range(len(str)):
    print (i)
'''
sub_str = [str1[i:j] for i in range(len(str1)) for j in range(i+1, len(str1)+1) ]
print (sub_str)

# OR #

prefix_sub_str = [str1[i:j] for i in range(len(str1)) for j in range(len(str1)+1) if i < j]
print(prefix_sub_str)

'''
['a', 'ab', 'abd', 'abda', 'abdab', 'abdabc', 'b', 'bd', 'bda', 'bdab', 'bdabc', 'd', 'da', 'dab', 'dabc', 'a', 'ab', 'abc', 'b', 'bc', 'c']
'''