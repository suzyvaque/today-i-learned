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

def get_square_sum(num):
    num_list = list(str(num))
    square_sum = 0
    for digit in num_list:
        square_sum += int(digit)**2
    return square_sum
    
n = int(input())
for num in range(2, n+1):
    if isPrime(num):
        square_sum = get_square_sum(num)
        prev_list = []
        prev_list.append(square_sum)
        
        self_repeating = False
        
        while self_repeating == False:
            square_sum = get_square_sum(square_sum)
            
            if square_sum == 1:
                print(num)
                break
            
            for prev in prev_list:
                if square_sum == prev:
                    self_repeating = True
                    break
            
            prev_list.append(square_sum)