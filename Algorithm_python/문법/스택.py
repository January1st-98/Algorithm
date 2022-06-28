# 기본적으로 제공되는 리스트를 이용해서 push(append), pop(pop) 연산을 이용해 스택으로 사용할 수 있다.
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력 [1, 3, 2, 5]
print(stack) # 최 하단 원소부터 출력 [5, 2, 3, 1]
