prices = {"beer": 2, "fish": 5, "apple": 1}

print (prices.items())
# another method of iteration 
for index, key in enumerate(prices): 
	print (index, key, prices[key] )


sort_dict = {}
for k in sorted(prices.keys()):
	sort_dict[k] = prices[k]

print(sort_dict)
valList = [11,22,33,44]
print(sort_dict.fromkeys(prices, prices.values()))
