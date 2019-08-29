n = 100
'''
evens = [ x for x in range(n) if x % 2 == 0 ]
print(evens)

odds = [ y for y in range(n) if y % 2 == 1 ]
print (odds)

even_odd = [[x,y] for x in range(5) for y in range(5)]
print(even_odd)
'''
num_squares = [(x,x**2) for x in range(5)]
print(num_squares)

