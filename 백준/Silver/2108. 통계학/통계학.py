import sys
input = sys.stdin.readline

N = int(input())
num = []
for _ in range(N):
    num.append(int(input()))
sum = 0
for item in num:
    sum += item
print(int(round(sum/N,0)))

sort_num = sorted(num)
print(sort_num[(N//2)])

if N != 1:
    most = 1
    cnt = []
    for i in range(N-1):
        if sort_num[i] == sort_num[i+1]:
            most +=1
        else:
            cnt.append([sort_num[i], most])
            most = 1
            
        if i == N-2 and sort_num[i] == sort_num[i+1]:
            cnt.append([sort_num[i], most])
    if sort_num[-1] != sort_num[-2]:
        cnt.append([sort_num[-1], 1])
    sort_cnt = sorted(cnt, key = lambda x : (x[1], -x[0]))
    if sort_cnt[-1][1] == sort_cnt[-2][1]:
        print(sort_cnt[-2][0])
    else:
        print(sort_cnt[-1][0])
else:
    print(num[0])

print(sort_num[-1]-sort_num[0])