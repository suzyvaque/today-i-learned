n, m = map(int, input().split())

baskets = [0 for i in range(n)]

for iteration in range(m):
    i, j, k = map(int, input().split())
    # i starts from 1
    for num in range(i-1, j):
        baskets[num] = k

print(*baskets)