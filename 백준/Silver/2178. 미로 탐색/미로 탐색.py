import sys
input= sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
map = []
for i in range(N):
    map.append(input().strip())
    
    
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

visited = [[-1 for _ in range(M)]for _ in range(N)]
queue = deque()
queue.append([0, 0]) # 행 열 카운트

visited[0][0] = 1

while(queue):
    row, col = queue.popleft()
    
    if (row == N-1 and col == M-1):
        print(visited[row][col])
        break
    
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        
        if(0 <= nr < N and 0 <= nc < M):
            if(map[nr][nc] == '1'):
                if (visited[nr][nc] == -1):
                    visited[nr][nc] = visited[row][col] + 1
                    queue.append([nr, nc])