import sys
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = list(map(int, sys.stdin.readline().split()))
graph = []
dist = []

for _ in range(n):
    graph.append(sys.stdin.readline().strip())
    dist.append([-1] * m)
queue = deque()
queue.append((0, 0))
dist[0][0] = 1
while len(queue) != 0:
    cur = queue.popleft()
    for dir in range(4):
        nx = cur[0] + dx[dir]
        ny = cur[1] + dy[dir]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if dist[nx][ny] > 0 or graph[nx][ny] == '0':
            continue
        queue.append((nx, ny))
        dist[nx][ny] = dist[cur[0]][cur[1]] + 1
print(dist[n-1][m-1])
