import sys
from collections import deque
m, n = list(map(int, sys.stdin.readline().split()))
graph = []
dist = []
queue = deque()
zero_count = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = -1
for _ in range(n):
    add_row = list(map(int, sys.stdin.readline().split()))
    graph.append(add_row)
    zero_count += add_row.count(0)

    dist.append([-1] * m)

# print(zero_count)
if zero_count == 0:
    print(0)
    sys.exit(0)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))
            dist[i][j] = 0

while len(queue) != 0:
    cur = queue.popleft()
    for dir in range(4):
        nx = cur[0] + dx[dir]
        ny = cur[1] + dy[dir]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if dist[nx][ny] >= 0 or graph[nx][ny] == -1:
            continue
        queue.append((nx, ny))
        dist[nx][ny] = dist[cur[0]][cur[1]] + 1
        ans = max(ans, dist[nx][ny])
        zero_count -= 1

# print(zero_count)
if zero_count != 0:
    print(-1)
else:
    print(ans)



