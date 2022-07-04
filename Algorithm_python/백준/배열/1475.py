import math
n = input()
numbers = [0] * 10
for ch in n:
    numbers[ord(ch) - ord('0')] += 1

ans = 0
for i in range(len(numbers)):
    if i == 6:
        ans = max(ans, math.ceil((numbers[6] + numbers[9]) / 2))
    elif i == 9:
        continue
    else:
        ans = max(ans, numbers[i])
print(ans)