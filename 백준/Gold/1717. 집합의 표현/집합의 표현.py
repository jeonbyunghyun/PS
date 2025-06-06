import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**8)

def find(x):
    if(parent[x] == x):
        return x
    parent[x] = find(parent[x])
    return parent[x]
    
def union(x, y):
    parent_x = find(x)
    parent_y = find(y)
    
    if(parent_x > parent_y):
        parent[parent_x] = parent_y
    elif(parent_x < parent_y):
        parent[parent_y] = parent_x
    else:
        return

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
for _ in range(M):
    query, a, b = map(int, input().split())
    if(query == 0):
        union(a, b)
    else: # 1
        if(find(a) == find(b)):
            print("YES")
        else:
            print("NO")