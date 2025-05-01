import sys
input = sys.stdin.readline

N = int(input())
end_num = '666'

title = [666, 1666, 2666, 3666, 4666, 5666, 6660]
cur = 6660
cnt = 7
t = ''
if (N <= 7):
    print(title[N-1])
else:
    while True:
        if (cnt == N):
            print(cur)
            break
        cur += 1
        if (end_num in str(cur)):
            cnt += 1
            t = cur
        