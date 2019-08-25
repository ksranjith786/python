evens = [i for i in (0, 100)]
print (evens)

evens = [i for i in [0, 100]]
print (evens)

evens = [i for i in range(0, 100)]
print (evens)

evens = [i for i in range(0, 100) if i % 2 == 0]
print (evens)

print()

# below list contains square of all odd numbers from 
# range 1 to 10
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1] 
print (odd_square )
  
# for understanding, above generation is same as, 
odd_square = [] 
for x in range(1, 11): 
    if x % 2 == 1: 
        odd_square.append(x**2) 
print (odd_square)

# below list contains power of 2 from 1 to 8 
power_of_2 = [2 ** x for x in range(1, 9)] 
print (power_of_2)

#primes = [x for x in range(1, 100, 2) if not(x % 3 == 0 or x % 5 == 0 or x % 7 == 0)]
#print (primes)

# below list contains prime and non-prime in range 1 to 50
start=2
stop=100 
noprimes = [j for i in range(start, 8) for j in range(i*start, stop, i)] 
print (noprimes)
primes = [x for x in range(start, stop) if x not in noprimes] 
print (primes) 