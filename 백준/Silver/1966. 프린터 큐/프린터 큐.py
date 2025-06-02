import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):

    N, M = map(int, input().split())
    input_data = list(map(int, input().split()))
    
    queue = deque()
    
    for idx in range(N):
        queue.append([input_data[idx], idx])
    
    sorted_queue = deque(sorted(queue, reverse=True))
    
    time = 1
    while(queue):
        max_value = sorted_queue[0][0]
        value, idx = queue.popleft()

        if (value == max_value): # 프린트
            sorted_queue.popleft()
            if (idx == M):
                print(time)
                break
            else:
                time += 1
        else: # 뒤로 넘김
            queue.append([value, idx])
               