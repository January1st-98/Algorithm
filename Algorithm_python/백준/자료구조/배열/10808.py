import sys
word = sys.stdin.readline().strip()
alphabet_count = [0] * 26
for ch in word:
    alphabet_count[ord(ch) - ord('a')] += 1
for cnt in alphabet_count:
    print(cnt, end=' ')


