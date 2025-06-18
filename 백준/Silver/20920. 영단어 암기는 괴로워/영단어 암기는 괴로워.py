import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())
word = defaultdict(int)
for _ in range(N):
    key = input().strip()
    if (len(key) >= M):
        word[key] += 1
wordlist = list(word.items())
wordlist.sort(key = lambda x : [-x[1], -len(x[0]), x[0]])

for item in wordlist:
    print(item[0])