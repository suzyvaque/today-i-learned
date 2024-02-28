n = int(input())
count = 0
num = 665

while True:
    num += 1

    if '666' in str(num):
        count += 1

    if count == n:
        break

print(num)

'''
Brute Force: complete search

Initially, thought about splitting the prob into two cases of having potential digits after 666 and not (n<=10), and setting a function that calculates the num.
But finding the function was just... -> Use Brute Force instead
'''