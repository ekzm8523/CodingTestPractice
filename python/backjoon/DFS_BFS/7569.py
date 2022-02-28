# https://www.acmicpc.net/problem/7569

from collections import deque


def bfs(tensor):
    move = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))  # K, M, N
    q = deque()
    ripe_cnt = 0
    empty_cnt = 0
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if tensor[h][r][c] == 1:
                    q.append((h, r, c, 0))
                    ripe_cnt += 1
                if tensor[h][r][c] == -1:
                    empty_cnt += 1

    while q:
        h, r, c, day = q.popleft()
        for dh, dr, dc in move:
            nh, nr, nc = h + dh, r + dr, c + dc
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and tensor[nh][nr][nc] == 0:
                tensor[nh][nr][nc] = 1
                q.append((nh, nr, nc, day + 1))
                ripe_cnt += 1
    return day if ripe_cnt == (M * N * H) - empty_cnt else -1


if __name__ == '__main__':
    M, N, H = map(int, input().split())

    # H * N * M
    tensor = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
    print(bfs(tensor))

