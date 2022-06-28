from collections import deque

queue = deque()

# 큐(Queue)구현을 위해 deque 라이브러리를 사용
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()
queue.pop()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse()
print(queue)