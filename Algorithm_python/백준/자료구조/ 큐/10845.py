import sys
queue = [] # empty queue
n = int(sys.stdin.readline())
for _ in range(n):
    operation = sys.stdin.readline().split()
    op = operation[0]
    if op == 'push':
        queue.append(int(operation[1]))
    elif op == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif op == 'size':
        print(len(queue))
    elif op == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif op == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
