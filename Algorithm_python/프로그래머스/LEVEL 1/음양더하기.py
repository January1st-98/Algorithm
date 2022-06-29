def solution(absolutes, signs):
    plus = sum([absolutes[i] for i in range(len(absolutes)) if signs[i]])
    minus = sum([absolutes[i] for i in range(len(absolutes)) if not signs[i]])
    return plus - minus

print(solution([4, 7, 12], [True, False, True]))