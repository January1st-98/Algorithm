import sys
n = int(sys.stdin.readline())
heights = list(map(int, sys.stdin.readline().split()))
tower = []
tower.append((1e9, 0))

for i in range(1, n+1):
    height = heights[i-1]
    while tower[-1][0] < height:
        tower.pop()
    print(f'{tower[-1][1]}', end=' ')
    heights.append((height, i))

