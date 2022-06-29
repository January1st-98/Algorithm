from itertools import combinations

def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = -1

    num_list = list(combinations(nums, 3))
    for num in num_list:
        print(isPrime(sum(num)))
        if isPrime(sum(num)):
            answer += 1

    return answer

print(solution([1,2,3,4]))