import sys
h, m = map(int, sys.stdin.readline().split())
m -= 45
if m < 0:
    m = 60 + m
    h -= 1
    if h < 0:
        h = 23
print('{} {}'.format(h, m))