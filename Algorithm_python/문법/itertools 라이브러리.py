
#itertools
#permutation
"""
리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)
을 계산해준다. permutations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여
사용한다.
"""
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 3)) # 모든 순열 구하기
print(result)

#combinations
"""
combinations는 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고
나열하는 모든 경우(조합(을 계산한다.
combinations 는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.
"""
from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기
print(result)

#product
"""
product는 permutaions와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아
일렬로 나열하는 모든 경우(순열)을 계산한다. 다만 원소를 중복하여 뽑는다 <- 중요
product 객체를 초기화 할때는 데이터의 수를 repeat 속성값으로 넣어준다.
product는 클래스이므로 객체초기화 이후에는 리스트 자료형으롭 변환하여 사용한다.
"""
from itertools import product

data = [1, 2, 3]
result = list(product(data, repeat=2))
print(result)

#combigation_with_replacement
"""
combinations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지
않고 나열하는 모든 경우(조합)을 계산한다.
다만 원소를 중복해서 뽑는다.
combination_with_replacement는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여
사용한다.
"""
from itertools import combinations_with_replacement
data = [1, 2, 3]
result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기(중복 허용)
print(result)