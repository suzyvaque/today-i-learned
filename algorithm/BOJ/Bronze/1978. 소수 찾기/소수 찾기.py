def isPrime(num):
    if num == 1:
        return False
        
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())
count = 0

numbers = list(map(int, input().split()))

for num in numbers:
    if isPrime(num):
        count += 1
        
print(count)