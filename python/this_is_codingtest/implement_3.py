
ins = input()

dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]

def is_out_of_index(x,y,dir):
    return 1 > x + dx[dir] or 8 < x + dx[dir] or 1 > y + dy[dir] or 8 < y + dy[dir]


x = ord(ins[0]) - ord('a') + 1
y = int(ins[1])
answer = 0
for i in range(8):
    if not is_out_of_index(x,y,i):
        answer+=1
print(answer)








