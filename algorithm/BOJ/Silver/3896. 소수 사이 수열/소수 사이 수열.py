'''
Sieve of Eratosthenes: Prime Number Search
'''

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True
    
n = int(input())
for i in range(n):
    testcase = int(input())
    length = 0
    if isPrime(testcase) == False:
        prime_small, prime_large = 0, 0
        
        for smaller in range(testcase-1, 2-1, -1):
            if isPrime(smaller):
                prime_small = smaller
                break
        
        for larger in range(testcase+1, 1299709+1):
            if isPrime(larger):
                prime_large = larger
                break
        
        length = prime_large - prime_small
        
    print(length)