import sys
n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())
ans = 0
numbers.sort()
for i1 in range(len(numbers) - 1):
    if numbers[i1] > x:
        break
    for i2 in range(i1 + 1, len(numbers)):
        if numbers[i2] > x:
            break
        if numbers[i1] + numbers[i2] == x:
            ans += 1
print(ans)