import sys
input = sys.stdin.readline

N = int(input())
stack = list()

def push(X : int):
     stack.append(X)
def pop():
    if(stack) :
        print(stack[-1])
        stack.pop()
    else :
        print(-1)
def size():
    print(len(stack))
def empty():
    if(stack):
        print(0)
    else:
        print(1)
def top():
    if (stack):
        print(stack[-1])
    else:
        print(-1)
for _ in range(N):
    cmd = input().split()
    
    if(cmd[0] == "push"):
        push(cmd[1])
    elif(cmd[0] == "pop"):
        pop()
    elif(cmd[0] == "size"):
        size()
    elif(cmd[0] == "empty"):
        empty()
    elif(cmd[0] == "top"):
        top()
    