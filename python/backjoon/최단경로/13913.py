from collections import deque

if __name__ == '__main__':
    pos1, pos2 = map(int, input().split())

    q = deque()
    q.append((pos1, 0))
    visit = set()
    visit.add(pos1)
    visit_depth = {pos1: 0}

    while q:
        current_pos, depth = q.popleft()
        if current_pos == pos2:
            break

        next_pos = current_pos + 1
        if next_pos not in visit:
            visit.add(next_pos)
            visit_depth[next_pos] = depth + 1
            q.append((next_pos, depth + 1))

        next_pos = current_pos - 1
        if next_pos not in visit:
            visit.add(next_pos)
            visit_depth[next_pos] = depth + 1
            q.append((next_pos, depth + 1))

        next_pos = current_pos * 2
        if next_pos not in visit:
            visit.add(next_pos)
            visit_depth[next_pos] = depth + 1
            q.append((next_pos, depth + 1))
    answer = [current_pos]
    while current_pos != pos1:
        if (current_pos - 1) in visit_depth and visit_depth[current_pos - 1] == (depth - 1):
            current_pos -= 1
        elif (current_pos + 1) in visit_depth and visit_depth[current_pos + 1] == (depth - 1):
            current_pos += 1
        elif (current_pos % 2) == 0 and (current_pos // 2) in visit_depth and visit_depth[current_pos // 2] == (depth - 1):
            current_pos //= 2
        depth -= 1
        answer.append(current_pos)
    print(*reversed(answer))

"""
input
5 17

output
4
5 10 9 18 17

input
5 17

output
4
5 4 8 16 17


"""