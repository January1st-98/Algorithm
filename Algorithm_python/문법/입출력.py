import sys
sys.setrecursionlimit(10**8) # 재귀의 깊이를 설정해주어야한다.
n = int(input())
print(n)

n = int(sys.stdin.readline()) # 숫자 하나 입력 input()은 비용이 크다.
print(n)

# 여러 데이터를 빈칸으로 구분해서 입력받을 경우
data = list(map(int, input().split()))
data.sort()
print(data)

# 더 빠른 방법 마지막의 rstrip()는 오른쪽의 개행문자를 제거해준다.
data = sys.stdin.readline().rstrip()
print(data)
