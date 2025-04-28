import sys
input = sys.stdin.readline

x = int(input())
a = x%3
if(a == 1):
    print("U")
elif(a == 2):
    print("O")
else:
    print("S")