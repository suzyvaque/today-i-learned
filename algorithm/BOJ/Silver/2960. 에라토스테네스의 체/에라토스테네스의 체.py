'''
Sieve of Eratosthenes: Prime Number Search
'''

def isPrime(num):
    if num == 1:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return False
    return True

n, k = map(int, input().split())
numbers = [True for i in range(n+1)]    # if erased, will be False
numbers[0], numbers[1] = False, False   # initially, 2 to n is True

count = 0
totalBreak = False
for num in range(2, n+1):
    if isPrime(num):
        for mul in range(1, int(n/num) + 1):
            if numbers[num*mul] == True:
                count += 1
                numbers[num*mul] = False
                # print(count, num*mul, "Erased")
            if count == k:
                print(num*mul)
                totalBreak = True
                break
    if totalBreak == True:
        break