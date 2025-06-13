import sys
input = sys.stdin.readline

def solve(num, length, path:list, result:list, start):
    if (len(path) == length):
        result.append(path[:])
        return

    for i in range(start, num):
        path.append(i+1)
        solve(num, length, path, result, i)
        path.pop()
    return result

N, M = map(int,input().split())

answer = solve(N, M, [], [], 0)
for item in answer:
    print(*item)