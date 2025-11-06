import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
ans = 0
for item in A:
    ans +=1
    rmn = item-B
    if rmn > 0:
        if rmn%C != 0:
            x = (rmn//C)+1
        else:
            x = rmn//C
        ans +=x

print(ans)