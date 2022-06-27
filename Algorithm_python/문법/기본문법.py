import sys

# 수의 지수표현
a = 1e9
a = 75.25e1
a - 3954e-3
print(a)

# 반올림 round 함수
print(round(123.456, 2)) # 123.46

# 리스트 컴프리헨션
# 0부터 9까지의 수 중에서 홀수만을 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [i**2 for i in range(10)]
print(array) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 2차원 리스트 초기화
n = 3
m = 3
array = [[0] * m for _ in range(n)]
print(array)

# 리스트 관련 메서드
base_list = [1, 2, 3]
base_list.reverse()
print(base_list)
print(base_list.count(1)) # 변수.count: 리스트에서 특정 값을 가지는 데이터 개수
base_list.remove(1)
print(base_list) # [3, 2]

a = [1, 2, 3, 4, 5]
remove_set = [1, 4]
result = [i for i in a if i not in remove_set] # [2, 3, 5]
print(result)

# 투플
data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['코코넛'] = 'coconut'

key_list = data.keys()
value_list = data.values()

for key in key_list:
    print(data[key])


