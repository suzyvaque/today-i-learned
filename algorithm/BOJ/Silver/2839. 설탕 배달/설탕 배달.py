'''
Brute Force
'''

n = int(input())

max_3 = int(n/3) + 1
max_5 = int(n/5) + 1

min_bags = max_3

for num_3 in range(0, max_3):
    for num_5 in range(0, max_5):
        if 3*num_3 + 5*num_5 == n:
            min_bags = min([min_bags, num_3+num_5])

if min_bags == max_3:
    # implausible; couldn't make exact n
    min_bags = -1

print(min_bags)