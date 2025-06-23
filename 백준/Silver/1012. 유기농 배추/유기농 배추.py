import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0 for _ in range(M)]for _ in range(N)]
    vegetables = []
    for _ in range(K):
        vegetables.append(list(map(int, input().split())))

    for vegetable in vegetables:
        board[vegetable[1]][vegetable[0]] = 1

    row = 0
    col = 0
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    visited = [[False for _ in range(M)]for _ in range(N)]
    stack = 0
    for i in range(M):
        for j in range(N):
            if (board[j][i] == 0):
                continue
            if (visited[j][i] == True):
                continue
            queue = deque()
            queue.append([j, i])
            visited[j][i] = True
            while(queue):
                row, col = queue.popleft()
                for k in range(4):
                    nr = row + dr[k]
                    nc = col + dc[k]
                    
                    if (0 <= nr < N and 0 <= nc < M):
                        if (board[nr][nc] == 1):
                            if (visited[nr][nc] == False):
                                queue.append([nr, nc])
                                visited[nr][nc] = True
            stack += 1
    print(stack)