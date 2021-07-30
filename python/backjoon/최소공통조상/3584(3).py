import sys

if __name__ == "__main__":

    test = int(sys.stdin.readline())

    for _ in range(test):
        n = int(sys.stdin.readline())
        parents = [None] + [0] * n

        for _ in range(n - 1):
            a, b = map(int, sys.stdin.readline().split())
            parents[b] = a

        a, b = map(int, sys.stdin.readline().split())
        a_parents = [a]
        b_parents = [b]

        while parents[a] > 0:
            a_parents.append(parents[a])
            a = parents[a]

        while parents[b] > 0:
            b_parents.append(parents[b])
            b = parents[b]

        size = min(len(a_parents), len(b_parents))
        answer = 0
        for i in range(1, size + 1):
            if a_parents[-i] == b_parents[-i]:
                answer = a_parents[-i]

        print(answer)