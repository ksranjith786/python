# Time complexity is O(1); Space Complexity is O(n)
# Memorization Technique
def fibonacci(n):
    """
    The fibonacci(n) is a function that returns the nth fibonacci number (assumes that series starts with 0; eg. 0,1,1,2,3, etc.)
    """
    fib = [0, 1]
    if n == 1:
        return fib[0]
    elif n == 2:
        return fib[1]
    else:
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])

#    print(len(fib))
    return fib[n-1]

# called by __main__
def driver():
    num = int(input("Enter a number: "))
    print(fibonacci(num))

# Python searches for this first instead of fibonacci or driver
if __name__ == "__main__":
    driver()

# Executes last
print ("Bye")
print (fibonacci.__doc__)
