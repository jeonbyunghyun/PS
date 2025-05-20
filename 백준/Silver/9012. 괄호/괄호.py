import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    stack = []
    input_datas = input().rstrip()
    is_possible = True
    
    for data in input_datas:
        if (data == '('):
            stack.append('(')
        else: # )
            if (len(stack) > 0):
                stack.pop()
            else:
                is_possible = False
                break
            
    if (is_possible and not stack):
        print("YES")
    else:
        print("NO")