import sys

t = int(input())

for iteration in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a+b)