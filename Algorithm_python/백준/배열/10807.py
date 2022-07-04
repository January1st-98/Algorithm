import sys
n = int(sys.stdin.readline())
numbers = [0] * 201
inputs = list(map(int, sys.stdin.readline().split()))
for num in inputs:
    numbers[num + 100] += 1

find_num = int(sys.stdin.readline())
print(numbers[find_num + 100])