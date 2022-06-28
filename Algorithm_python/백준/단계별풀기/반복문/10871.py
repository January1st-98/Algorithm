import sys
t, n = map(int, sys.stdin.readline().split())
print(nums)
for num in nums:
    if num < n:
        print(f'{num}', end=' ')
