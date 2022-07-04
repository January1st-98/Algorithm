import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
result = str(a * b * c)
number_count = [0] * 10
for ch in result:
    number_count[ord(ch) - ord('0')] += 1
for number in number_count:
    print(number)

