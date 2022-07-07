from collections import deque
import sys

n = int(sys.stdin.readline())
deque = deque([i for i in range(1, n+1)])
deque.rotate(-1)
print(deque)