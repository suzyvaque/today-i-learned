import queue

"""
import logging
import inspect
logging.basicConfig(filename = "debug-2178.log", level = logging.DEBUG)
def log(varName, var):
    logging.debug(f"line {inspect.currentframe().f_lineno}")
    logging.debug(f"{varName} : {var}\n")
"""

n, m = map(int, input().split())
# will have n lines of input with m numbers each
graph = [list(input()) for _ in range(n)]

visited = [[0 for _ in range(m)] for _ in range(n)]

q = queue.Queue()
# for adjacent node check
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# starting point
q.put([0, 0])
visited[0][0] = 1

while q.empty() == False:
    # bfs. in this prob, nodeAdj for (x,y) becomes (x-1,y), (x,y+1), (x+1,y), (x,y-1)
    # pop current node
    x, y = q.get()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # log("nx, ny", [nx,ny])
        """
        Before putting in queue, should check 3 bfs conditions
        """

        # 1. out of range
        if nx < 0 or nx >= n:
            continue
        if ny < 0 or ny >= m:
            continue
        # 2. is not connected, cannot visit
        if graph[nx][ny] == "0":
            # FIXME list(input()) so all the values are string...
            continue
        # 3. already visited
        if visited[nx][ny] != 0:
            continue

        # in visited: if 0, unvisited. else, the number will indicate the level in graph.
        # level == distance from root (starting point)
        # child = parent + 1
        visited[nx][ny] = visited[x][y] + 1
        q.put([nx, ny])
        # log("visited", visited)

print(visited[n-1][m-1])