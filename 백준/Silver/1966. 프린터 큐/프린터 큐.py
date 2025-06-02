import sys
import heapq
from collections import deque
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):

    N, M = map(int, input().split())
    input_data = list(map(int, input().split()))
    
    queue = deque()
    heap = []
    
    for idx in range(N):
        queue.append([idx, input_data[idx]])
        heapq.heappush(heap, -input_data[idx])

    time = 1
    while(heap and queue):
        max_value = -heap[0]
        idx, value = queue.popleft()

        if (value == max_value): # 프린트
            heapq.heappop(heap)
            if (idx == M):
                print(time)
                break
            else:
                time += 1
        else: # 뒤로 넘김
            queue.append([idx, value])
               