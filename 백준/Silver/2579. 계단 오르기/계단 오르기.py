import sys
input = sys.stdin.readline

N = int(input())

stairs = []
for _ in range(N):
    stairs.append(int(input()))

if N == 1:
    print(stairs[0])
    exit(0)
if N == 2:
    print(stairs[0] + stairs[1])
    exit(0)
if N == 3:
    print(max(stairs[1] + stairs[2], stairs[0] + stairs[2]))
    exit(0)

dp = [[0 for i in range(2)] for i in range(N)]
dp[0][0] = stairs[0]
dp[1][0] = stairs[0] + stairs[1]
dp[1][1] = stairs[1]
dp[2][0] = stairs[1] + stairs[2]
dp[2][1] = stairs[0] + stairs[2]

for i in range(3, N):
    dp[i][0] = dp[i-1][1] + stairs[i]
    dp[i][1] = max(dp[i-2]) + stairs[i]
print(max(dp[-1]))