import sys
score = int(sys.stdin.readline())
if score >= 90 and score <= 100:
    print('A', end='')
elif score >= 80 and score <= 89:
    print('B', end='')
elif score >= 70 and score <= 79:
    print('C', end='')
elif score >= 60 and score <= 69:
    print('D', end='')
else:
    print('F', end='')