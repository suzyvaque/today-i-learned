a, b, c, d, e, f = map(int, input().split())
min = -999
max = 999

for x in range(min, max+1):
    for y in range(min, max+1):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y, sep=" ")