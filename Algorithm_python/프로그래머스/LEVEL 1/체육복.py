def solution(n, lost, reserve):
    answer = 0
    uniform = [1] * (n + 1)
    for i in reserve:
        uniform[i] += 1
    for l in lost:
        uniform[l] -= 1
    answer = n - uniform.count(0)  # 전체 학생 수에서 유니폼을 가지고 있지 않은 학생을 뺀다. -> 현재 체육복을 가지고 있는 학생 수
    for i in range(1, n+1):
        if uniform[i] == 0:
            if i - 1 >= 1:
                if uniform[i - 1] == 2:
                    uniform[i - 1] -= 1
                    uniform[i] += 1
                    answer += 1
            elif i + 1 <= len(uniform):
                if uniform[i + 1] == 2:
                    uniform[i + 1] -= 1
                    uniform[i] += 1
                    answer += 1
    return answer

print(solution(5, [2, 4], [1, 3, 5]))