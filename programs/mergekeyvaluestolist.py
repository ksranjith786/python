list1 = [ {'key1':12, 'key2':14, 'key4':32} \
    ,{'key5':18, 'key3':54, 'key8':20} \
    ,{'key2':22, 'key4':31, 'key1':82} \
    ,{'key3':41, 'key5':18, 'key2':14} ]

# print (list1)


res = {} # or res = dict()
'''
for s in list1:
    for k,v in s.items():
        if k in res.keys():
            vals = res.get(k)
            vals.append(v)
        else:
            res[k] = [v]
'''

for subset in list1:
    for k,v in subset.items():
        res.setdefault(k, []).append(v)

print(res)
'''
res1 = { (key,val) for set1 in list1 for key,val in set1.items() }
print (res1)
'''

res1 = [ key: list([key for subset in list1 for key in subset.keys]) ]