from collections import deque
import sys
n = int(sys.stdin.readline())
for _ in range(n):
    operation = list(sys.stdin.readline())
    number = int(sys.stdin.readline())
    command = sys.stdin.readline().strip().lstrip('[').rstrip(']')
    if command == '':
        input = deque()
    else:
        input = deque(command.split(','))
    isReversed = False
    isError = False
    for op in operation:
        if op == 'R':
            isReversed = not isReversed
        elif op == 'D':
            if len(input) == 0:
                isError = True
                break
            else:
                if isReversed:
                    input.pop()
                else:
                    input.popleft()

    if isError:
        print('error')
        continue
    if isReversed:
        input.reverse()
    print('[' + ','.join(input) +']')

