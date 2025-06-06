import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
import heapq

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if (x < y):
        parent[y] = x
        return True
    elif (x > y):
        parent[x] = y
        return True
    else:
        return False

N = int(input())
parent = [i for i in range(N)]

edges = []
for i in range(N):
    a = list(map(int, input().split()))
    for j in range(i+1, N):
        heapq.heappush(edges, [a[j], i, j])
        
answer = 0

while (edges):
    edge = heapq.heappop(edges)
    if (union(edge[1], edge[2])):
        answer += edge[0]
print(answer)