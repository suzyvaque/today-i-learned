import queue

def bfs(startX, startY):
    q = queue.Queue()
    visited[startX][startY] = 1
    q.put([startX, startY])

    while q.empty() == False:
        x, y = q.get()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= l:
                continue
            if ny < 0 or ny >= l:
                continue
            if visited[nx][ny] != 0:
                continue

            visited[nx][ny] = visited[x][y] + 1
            q.put([nx, ny])

            if nx == desX and ny == desY:
                # should print the level, not the coord itself!!!
                # level-1, since we've assigned root as level 1
                print(visited[nx][ny]-1)
                return


tests = int(input())
dx = [1, -1, 1, -1, 2, -2, 2, -2]
dy = [2, -2, -2, 2, 1, -1, -1, 1]

for _ in range(tests):
    l = int(input())
    curX, curY = map(int, input().split())
    desX, desY = map(int, input().split())

    if curX == desX and curY == desY:
        # should always consider this case!
        print(0)
        continue

    visited = [[0 for _ in range(l)] for _ in range(l)]
    bfs(curX, curY)
