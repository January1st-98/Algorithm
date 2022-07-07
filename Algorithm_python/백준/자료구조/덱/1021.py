from collections import deque
import sys

n, m = list(map(int, sys.stdin.readline().split()))
numbers = list(map(int, sys.stdin.readline().split()))
deque = deque([i for i in range(1, n+1)])
ans = 0
for num in numbers:
    # print(deque)
    forward_idx = 0
    backward_idx = 0
    cnt = 0
    while True:
        if deque[forward_idx] == num:
            deque.rotate(-forward_idx)
            deque.popleft()
            ans += cnt
            break
        elif deque[backward_idx] == num:
            deque.rotate(-backward_idx)
            deque.popleft()
            ans += cnt
            break
        cnt += 1
        forward_idx += 1
        backward_idx -= 1

print(ans)
