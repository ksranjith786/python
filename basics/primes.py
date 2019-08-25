# below list contains prime and non-prime in range 1 to 50
start=2
stop=100 

# prime numbers in 1 to 100
primes = [2, 3, 5, 7]
primes += ([x for x in range(11, 100, 2) if not(x % 3 == 0 or x % 5 == 0 or x % 7 == 0)])
print (primes)

noprimes = [j for i in range(start, 8) for j in range(i*start, stop, i)] 
print (noprimes)
primes = [x for x in range(start, stop) if x not in noprimes] 
print (primes) 
