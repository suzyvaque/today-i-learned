def permutation(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in permutation(arr[:i]+arr[i+1:], r-1):
                yield [arr[i]] + next

n, m = map(int, input().split())
arrN = [i for i in range(1, n+1)]
combs = list(permutation(arrN, m))
for comb in combs:
    print(*comb)