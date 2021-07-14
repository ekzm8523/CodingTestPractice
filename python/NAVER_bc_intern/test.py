
def solution(A):
    A.sort()
    idx = 1
    for value in A:
        if value < idx:
            continue
        elif value == idx:
            idx += 1
        else:
            return idx
    return idx
if __name__ == "__main__":
    A = [1, 3, 6, 4, 1, 2]
    print(solution(A))
    A = [1, 2, 3]
    print(solution(A))
    A = [-1, -3]
    print(solution(A))