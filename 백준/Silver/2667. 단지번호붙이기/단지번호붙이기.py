import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

map = []

for _ in range(N):
    map.append(input().strip())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

visited = [[-1 for _ in range(N)] for _ in range(N)]
answer = []
for i in range(N):
    for j in range(N):
        if (map[i][j] == '0'):
            continue
        
        if (visited[i][j] != -1):
            continue
        
        # bfs
        queue = deque()          
        queue.append([i, j])
        cnt = 1
        
        visited[i][j] = 1
        
        while(queue):
            row, col = queue.popleft()
            
            for k in range(4):
                nr = row + dr[k]
                nc = col + dc[k]
                if (0 <= nr < N and 0 <= nc < N):
                    if (map[nr][nc] == '1'):
                        if (visited[nr][nc] == -1):
                            queue.append([nr, nc])
                            cnt += 1
                            visited[nr][nc] = 1
        answer.append(cnt)
answer.sort()
print(len(answer))
for item in answer:
    print(item)
