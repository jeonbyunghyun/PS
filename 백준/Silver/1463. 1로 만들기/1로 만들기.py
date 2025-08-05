import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

dp = deque()
dp.append(N)
answer = 0
while(1 not in dp):
    answer += 1
    length = len(dp)
    for i in range(length):        
        if dp[i]% 3 == 0 and dp[i]/3 not in dp:
            dp.append(dp[i]/3)
        if dp[i] % 2 == 0 and dp[i]/2 not in dp:
            dp.append(dp[i]/2)
        if dp[i]-1 not in dp:
            dp.append(dp[i]-1)
print(answer)