import sys
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())

C = A//2 + B

if(N >= C):
    print(C)
    
else:
    print(N)