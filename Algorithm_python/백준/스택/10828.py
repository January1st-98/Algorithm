import sys
n = int(sys.stdin.readline())
s = [] # stack
for _ in range(n):
    operation = sys.stdin.readline().split()
    op = operation[0]
    if op == 'push':
        number = int(operation[1])
        s.append(number)
    elif op == 'pop':
        if len(s) != 0:
            print(s.pop())
        else:
            print(-1)
    elif op == 'size':
        print(len(s))
    elif op == 'empty':
        if len(s) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])