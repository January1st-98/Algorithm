import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))

maximum = -1e9
minimum = 1e9

def dfs(value, count):
    global maximum, minimum
    if count == n:
        # print(f'value: {value}')
        maximum = max(value, maximum)
        minimum = min(value, minimum)
        return

    for i in range(4):
        if operator[i] == 0:
            continue
        operator[i] -= 1

        if i == 0:
            dfs(value + numbers[count], count + 1)
        elif i == 1:
            dfs(value - numbers[count], count + 1)
        elif i == 2:
            dfs(value * numbers[count], count + 1)
        elif i == 3:
            dfs(int(value / numbers[count]), count + 1)

        operator[i] += 1

dfs(numbers[0], 1)
print(maximum, minimum)

