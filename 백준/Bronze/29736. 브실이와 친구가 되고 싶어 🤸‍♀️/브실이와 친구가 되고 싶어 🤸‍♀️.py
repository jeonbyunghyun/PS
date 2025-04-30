import sys
input = sys.stdin.readline

A, B = map(int, input().split())
K, X = map(int, input().split())

if(K+X <= B and A <= (K-X)):
    print((X*2)+1)
elif(K-X <= A and K+X >= B):
    print(B-A+1)
elif(K-X <= A <= K+X and K-X >=0):
    print((K+X)-A+1)
elif(K-X <= A <= K+X and K-X <0):
    print(K+X-A+1)
elif(K-X <= B <= K+X):
    print(B-(K-X)+1)
else:
    print("IMPOSSIBLE")