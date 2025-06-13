import sys
input = sys.stdin.readline

def solve(x, y, path:list, result:list):
    if (len(path) == y):
        result.append(path[:])
        return
        
    for i in range(x):
        path.append(i+1)
        solve(x, y, path, result)
        path.pop()
    return result

N, M = map(int, input().split())

answer = solve(N, M, [], [])
for item in answer:
    print(*item)