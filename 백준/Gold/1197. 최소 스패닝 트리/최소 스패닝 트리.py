import sys
input= sys.stdin.readline
sys.setrecursionlimit(1000000)

def find(x):
    if (parent[x] == x):
        return x
    parent[x] = find(parent[x])
    return parent[x] 

def union(x, y):
    global ch
    x = find(x)
    y = find(y)
    
    if (x < y):
        parent[y] = x
        ch = 1
    elif (x >y):
        parent[x] = y
        ch = 1
    else:
        return

V, E = map(int, input().split())
parent = [i for i in range(V+1)]
edges = []
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append([A, B, C])
edges.sort(key = lambda x : x[2])
ch = 0
answer = 0
for i in range(E):
    union(edges[i][0], edges[i][1])
    if (ch == 1):
        answer += edges[i][2]
        ch = 0
print(answer)