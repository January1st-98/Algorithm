import sys
count = [0] * 6
answer = 0
a, b, c = map(int, sys.stdin.readline().split())
count[a-1] += 1
count[b-1] += 1
count[c-1] += 1
max_value = max(a, b, c)
for i in range(6):
    if count[i] == 3:
        answer += 10000 + (i+1) * 1000
        break;
    elif count[i] == 2:
        answer += 1000 + (i+1) * 100
        break;
if answer == 0:
    answer += max_value * 100

print(answer)
