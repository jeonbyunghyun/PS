import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    fuck = input()
    stack = list()
    for i in range(len(fuck)) :
        if ( fuck[i] == "(" ):
            stack.append(1)
        elif( fuck[i] == ")"):
            if (len(stack) == 0):
                stack.append(1)
                break
            else :
                stack.pop()
    if (len(stack) == 0) :
        print("YES")
    else : 
        print("NO")