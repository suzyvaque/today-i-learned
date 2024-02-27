n, m = map(int, input().split())
listA = [[0 for i in range(m)] for i in range(n)]
listB = [[0 for i in range(m)] for i in range(n)]

for num in range(n):
    listA[num] = input().split()
for num in range(n):
    listB[num] = input().split()

for i in range(n):
    for j in range(m):
        listA[i][j] = int(listA[i][j]) + int(listB[i][j])
    print(*listA[i])