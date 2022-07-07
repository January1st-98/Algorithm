import sys
n = int(sys.stdin.readline())
s = [] # stack
for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        s.pop()
    else:
        s.append(num)
ans = 0
for num in s:
    ans += num
print(ans)
