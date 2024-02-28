n, m = map(int, input().split())
cards = list(map(int, input().split()))

max = 0

for i in range(len(cards)):
    for j in range(i+1, len(cards)):
        for k in range(j+1, len(cards)):
            num = cards[i] + cards[j] + cards[k]
            if max < num <= m:
                max = num

print(max)