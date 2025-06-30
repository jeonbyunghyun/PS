import sys
input = sys.stdin.readline

N = int(input())

five_kg = N//5
remain = N%5
while(1):
    if remain%3 != 0:
        remain+=5
        five_kg-=1
    elif five_kg < 0:
        print(-1)
        break
    else:
        three_kg = remain//3
        print(three_kg+five_kg)
        break