
def get_pi(p):
    m = len(p)
    j = 0
    pi = [0] * m
    for i in range(1, m):
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi


def kmp(s, p):

    ans = []
    n = len(s)
    m = len(p)
    j = 0
    pi = get_pi(p)

    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = pi[j - 1]
        if s[i] == p[j]:
            if j == m - 1:
                ans.append(i - m + 1)
                j = pi[j]
            else:
                j += 1
    return ans

if __name__ == "__main__":
    T = input()
    P = input()


    matched = kmp(T, P)
    print(len(matched))

    for match in matched:
        print(match + 1, end=" ")

    print()


