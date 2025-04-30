import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))

x = 0
min_diff = 300000
for a in range (0,N-2):
    for b in range (a+1,N-1):
        for c in range (b+1,N):
            if(0 <= M-(num[a]+num[b]+num[c]) < min_diff):
                min_diff = M - (num[a]+num[b]+num[c])
                x= num[a]+num[b]+num[c]
print(x)