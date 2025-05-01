import sys
input = sys.stdin.readline

N = int(input())
arr = list(set([input().rstrip() for _ in range(N)]))
arr.sort(key = lambda item : [len(item), item])

for item in arr:
    print(item)