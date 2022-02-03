from collections import deque

if __name__ == '__main__':
    test_case = int(input())
    for _ in range(test_case):
        n = int(input())
        value_error = False
        init_ranking = list(map(int, input().split()))
        in_degree = [0] * (n + 1)
        remove_dict = {}
        node_set = set(range(1, n + 1))

        for i, node in enumerate(init_ranking):
            in_degree[node] = i
            node_set.remove(node)
            remove_dict[node] = list(node_set)

        change_rank_case = int(input())

        for _ in range(change_rank_case):
            a, b = map(int, input().split())
            if init_ranking.index(a) < init_ranking.index(b):
                a, b = b, a

            remove_dict[b].remove(a)
            remove_dict[a].append(b)
            in_degree[a] -= 1
            in_degree[b] += 1

        q = deque()
        for i in range(1, n+1):
            if in_degree[i] == 0:
                q.append(i)

        remove_count = 0
        answer = []
        while q:
            node = q.popleft()
            answer.append(node)
            for remove_node in remove_dict[node]:
                in_degree[remove_node] -= 1
                if in_degree[remove_node] == 0:
                    q.append(remove_node)
            remove_count += 1

        print(*answer) if remove_count == n else print("IMPOSSIBLE")
