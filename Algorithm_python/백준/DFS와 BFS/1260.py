#https://www.acmicpc.net/problem/1260
import sys
from collections import deque
def dfs(graph, v, dfs_visited):
    dfs_visited[v] = True
    print(v, end=' ')
    for node in graph[v]:
        if not dfs_visited[node]:
            dfs(graph, node, dfs_visited)

def bfs(graph, v, bfs_visited):
    bfs_visited[v] = True
    queue = deque([v])
    while queue:
        cur = queue.popleft()
        print(cur, end=' ')
        for i in graph[cur]:
            if not bfs_visited[i]:
                bfs_visited[i] = True
                queue.append(i)


n, m, v = map(int, sys.stdin.readline().split())
visited = [False] * (n+1)
graph = [[] for _ in range(n + 2)]
dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

dfs(graph, v, dfs_visited)
print()
bfs(graph, v, bfs_visited)

