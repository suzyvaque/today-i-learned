import queue

n = int(input())
v = int(input())
graph = [list() for _ in range(n+1)]
for _ in range(v):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False for _ in range(n+1)]

def bfs(start):
    q = queue.Queue()
    count = 0

    visited[start] = True
    q.put(start)
    # count += 1    # Nope. The number of computers infected BY 1.

    while q.empty() == False:
        nodeCurr = q.get()
        for nodeAdj in graph[nodeCurr]:
            if visited[nodeAdj] == False:
                visited[nodeAdj] = True
                q.put(nodeAdj)
                count += 1

    return count

print(bfs(1))