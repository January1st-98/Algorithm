# https://www.acmicpc.net/problem/2525
import sys
h, m = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

m += t
if m >= 60:
    h += m / 60
    m = m % 60
    if h >= 24:
        h = h % 24
print('{} {}'.format(int(h), int(m)))