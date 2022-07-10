import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = list(map(int, sys.stdin.readline().split()))
board = []
vis = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
    vis.append([False] * m)
cnt = 0
max_area = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0 or vis[i][j]:
            continue
        queue = deque()
        queue.append((i, j))
        area = 0
        cnt += 1
        vis[i][j] = True
        while len(queue) != 0:
            cur = queue.popleft()
            area += 1
            for dir in range(4):
                nx = cur[0] + dx[dir]
                ny = cur[1] + dy[dir]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if vis[nx][ny] or board[nx][ny] == 0:
                    continue
                queue.append((nx, ny))
                vis[nx][ny] = True
        max_area = max(max_area, area)
print(cnt)
print(max_area)

