import sys
input = sys.stdin.readline

a, b = map(int, input().split())

x, y = max(a,b), min(a,b)
while(1):
    x,y = y, x%y
    if(y == 0):
        break

print(x)
print(int(a*b/x))