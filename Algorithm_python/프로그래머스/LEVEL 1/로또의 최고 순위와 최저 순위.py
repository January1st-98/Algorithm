def rank(correct):
    if correct == 0 or correct == 1:
        return 6
    else:
        return 7 - correct

def solution(lottos, win_nums):
    answer = []
    zero_count = lottos.count(0)
    correct = 0
    for num in lottos:
        for win_num in win_nums:
            if num == win_num:
                correct += 1
    answer.append(rank(correct + zero_count))
    answer.append(rank(correct))

    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))