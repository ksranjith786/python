primes = [2, 3, 5, 7]
primes += [ i for i in range(11, 100, 2) if not (i % 3 == 0 or i % 5 == 0 or i % 7 == 0) ]
print (primes)
print (len(primes))