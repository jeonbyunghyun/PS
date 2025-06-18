import sys
input = sys.stdin.readline

N, H = map(int, input().split())
des1 = [0 for _ in range(H+2)]
des2 = [0 for _ in range(H+2)]
ob1 = [0 for _ in range(H+2)]
ob2 = [0 for _ in range(H+2)]
for i in range(N):
    if (i%2 == 0):
        ob1[int(input())] += 1
    elif (i%2 == 1):
        ob2[int(input())] += 1
for i in range(2, len(ob1)):
    des1[-i] += des1[-i+1] + ob1[-i]
for i in range(1, len(ob2)-1):
    des2[i] = des2[i-1] + ob2[-i-1]
destroy = [0 for _ in range(H)]
for i in range(H):
    destroy[i] = des1[i+1] + des2[i+1]
minimum = min(destroy)
print(minimum, destroy.count(minimum))