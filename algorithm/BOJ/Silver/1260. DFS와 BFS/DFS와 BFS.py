import queue

n,m,v = map(int, input().split())
graph = [list() for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for l in graph:
    l.sort()

bfslist = list()
dfslist = list()

def bfs(start):
    q = queue.Queue()
    q.put(start)
    visited[start] = True
    bfslist.append(start)

    while q.empty() == False:
        nodeCurr = q.get()

        for nodeAdj in graph[nodeCurr]:
            if visited[nodeAdj] == False:
                bfslist.append(nodeAdj)
                visited[nodeAdj] = True
                q.put(nodeAdj)

def dfs(nodeCurr):
    visited[nodeCurr] = True
    dfslist.append(nodeCurr)

    for nodeAdj in graph[nodeCurr]:
        if visited[nodeAdj] == False:
            dfs(nodeAdj)

visited = [False for _ in range(n+1)]
dfs(v)
visited = [False for _ in range(n+1)]
bfs(v)
print(*dfslist)
print(*bfslist)

