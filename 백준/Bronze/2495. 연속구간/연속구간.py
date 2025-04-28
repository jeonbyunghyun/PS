import sys
input = sys.stdin.readline

A = input()
B = input()
C = input()


def read(D):
    N = 0
    x = 0
    y = 0
    for i in range (7):
        if (D[i] == D[i+1]):
            N+=1
            if(i == 6):
                y = N
            
        else:
            if(x<=N):
                x = N
                N = 0
    return(max(x,y)+1)

print(read(A))
print(read(B))
print(read(C))
