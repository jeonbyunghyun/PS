import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(input().strip()) for _ in range(N)]
aaa = 64

for r in range (N-7):
    for c in range(M-7):
        board = [[0 for _ in range(8)] for _ in range(8)]
        ch1 = 0
        ch2 = 0
        for a in range(8):
            for b in range(8):
                board[a][b] = arr[r+a][c+b]
                if((a+b)%2 == 0):
                    if(board[a][b] == 'B'):
                        ch1 += 1
                    elif(board[a][b] == 'W'):
                        ch2 += 1
                elif((a+b)%2 == 1):
                    if (board[a][b] == 'W'):
                        ch1 += 1
                    elif(board[a][b] == 'B'):
                        ch2 += 1
        if(aaa > min(ch1, ch2)):
            aaa = min(ch1, ch2)
            
print(aaa)