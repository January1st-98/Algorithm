def solution(participant, completion):
    answer = ''
    dic = dict()
    for part in participant:
        print(f'part: {part}')
        if part in dic:
            dic[part] += 1
        else:
            dic[part] = 1
    print(dic)
    for com in completion:
        dic[com] -= 1
    for key, value in dic.items():
        if dic[key] > 0:
            answer = value

    return answer

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))