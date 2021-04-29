
dx = [-1,0,1,0]
dy = [0,1,0,-1]

n = int(input())
ins = input().split()
x = 1
y = 1

def moveXY(x,y,dir):
    if 0 < (x + dx[dir]) <= n:
        x += dx[dir]
    if 0 < (y + dy[dir]) <= n:
        y += dy[dir]
    return x,y



for i in ins:
    print(i)
    print(x,y)
    if i == 'U':
        x,y = moveXY(x,y,0)
    elif i == 'R':
        x,y = moveXY(x,y,1)
    elif i == 'D':
        x,y = moveXY(x,y,2)
    elif i == 'L':
        x,y = moveXY(x,y,3)

print(x,y)
