import sys
t = int(sys.stdin.readline())
while t > 0:
    a, b = map(int, sys.stdin.readline().split())
    print(f'{a+b}')
    t -= 1