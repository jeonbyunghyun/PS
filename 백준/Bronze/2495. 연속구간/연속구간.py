import sys
input = sys.stdin.readline

A = input()
B = input()
C = input()


def read(D):
    N = 0
    x = 0
    for i in range (7):
        if (D[i] == D[i+1]):
            N = N + 1
            x = max(x, N)
        else:
            N = 0
        
    return(x+1)

print(read(A))
print(read(B))
print(read(C))