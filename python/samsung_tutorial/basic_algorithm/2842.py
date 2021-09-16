# https://www.acmicpc.net/problem/2842
import sys
from collections import deque
"""
일단 가장 고도차이가 덜나는 곳으로 간다는게 최적의 해를 보장해주지 않는다 -> 그리디 X
"""
dx = [-1, -1, 0, 1, 1,  1,  0, -1] # 시계방향
dy = [ 0,  1, 1, 1, 0, -1, -1, -1]

if __name__ == "__main__":

    n = int(sys.stdin.readline())
    table = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
    tired_table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    tired_ontology = set()
    total_house_cnt = 0

    for i in range(n):
        for j in range(n):
            if table[i][j] == 'P':
                px, py = i, j
            elif table[i][j] == 'K':
                total_house_cnt += 1
            tired_ontology.add(tired_table[i][j])
    tired_ontology = sorted(tired_ontology)
    ontology_size = len(tired_ontology)
    # 여기부터 투포인터를 사용해서 최대 피로도를 설정
    l, r = 0, 0
    answer = sys.maxsize
    while l < ontology_size:
        visit = [[False] * n for _ in range(n)]
        tired = tired_table[px][py]
        visited_house_cnt = 0
        dq = deque()
        is_valid = False
        if tired_ontology[l] <= tired <= tired_ontology[r]:
            visit[px][py] = True
            dq.append((px, py))
        while dq:
            x, y = dq.popleft()
            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                    tired = tired_table[nx][ny]
                    if tired_ontology[l] <= tired <= tired_ontology[r]:
                        dq.append((nx, ny))
                        visit[nx][ny] = True
                        if table[nx][ny] == 'K':
                            visited_house_cnt += 1
                            if visited_house_cnt == total_house_cnt:
                                is_valid = True
                                dq.clear()
        if is_valid:
            answer = min(answer, tired_ontology[r] - tired_ontology[l])
            l += 1
        else:
            r += 1
            if r == ontology_size:
                break
    print(answer)