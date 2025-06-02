import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    arr = []
    N, M = map(int, input().split())
    ipt = deque(list(map(int, input().split())))
    ipt[M] += 10
    
    while(1):
        max_ipt = max([x % 10 for x in ipt])    
        if((ipt[0])%10 < max_ipt):
            ipt.append(ipt[0])
            ipt.popleft()
        else:
            arr.append(ipt[0])
            ipt.popleft()
        if(len(ipt) == 0):
            break
    print(*[i+1 for i, value in enumerate(arr) if value> 10])