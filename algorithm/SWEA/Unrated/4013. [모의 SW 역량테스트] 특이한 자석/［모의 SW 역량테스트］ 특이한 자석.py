import queue


def rotate(num, dir):
    if alreadyMoved[num]:
        return

    # If you read the example carefully, you could have noticed that the magnets move ONLY ONCE...
    alreadyMoved[num] = True

    magnet_original = [val for val in magnets[num]]

    if dir == 1:
        for i in range(8):
            magnets[num][(i + 1) % 8] = magnet_original[i]
    elif dir == -1:
        for i in range(8):
            magnets[num][(i + 7) % 8] = magnet_original[i]

    # has left
    if num > 0:
        if magnets[num - 1][2] != magnet_original[6]:
            # should also rotate left magnet
            q.put([num - 1, dir * (-1)])
    # has right
    if num < 3:
        if magnet_original[2] != magnets[num + 1][6]:
            # should also rotate right magnet
            q.put([num + 1, dir * (-1)])

def getScore():
    score = 0
    for num in range(4):
        index0 = magnets[num][0]
        if index0 == 1:
            score += 2 ** num
    return score

t = int(input())
for test in range(t):
    k = int(input())
    magnets = [list(map(int, input().split())) for _ in range(4)]
    q = queue.Queue()

    for rotation in range(k):
        num, dir = map(int, input().split())
        q.put([num-1, dir])

        alreadyMoved = [False for _ in range(4)]
        while q.empty() == False:
            n, d = q.get()
            rotate(n, d)
            
    print(f"#{test+1} {getScore()}")
