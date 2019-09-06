'''
Input : string a = remuneration
        string b = acquiesce
        length of pre/suffix(l) = 5
Output :remuniesce

Input : adulation
        obstreperous
        6
Output :adulatperous
'''

l = 5
str1 = "remuneration"
str2 = "acquiesce"

i = l
j = len(str2) - l
res = str1[0:l] + str2[j:]
print (res)