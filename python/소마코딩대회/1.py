import sys
input = lambda: sys.stdin.readline().strip()


def main():
    # input
    object_cnt, pointer_cnt, query_cnt = map(int, input().split())
    pointers = [0] + [int(input()) for _ in range(pointer_cnt)]
    queries = []
    for _ in range(query_cnt):
        line = input()
        if line[0] == "r":
            query, x = line.split()
            queries.append((query, int(x), None))
        else:
            query, x, y = line.split()
            queries.append((query, int(x), int(y)))

    for query, x, y in queries:
        if query[0] == "a":  # assign
            pointers[x] = pointers[y]
        elif query[0] == "s":  # swap
            pointers[x], pointers[y] = pointers[y], pointers[x]
        elif query[0] == "r":  # reset
            pointers[x] = 0
        else:
            raise Exception("뭔가 이상하다..")
    remain_objects = set()

    for pointed_object in pointers:
        if pointed_object != 0:
            remain_objects.add(pointed_object)

    print(len(remain_objects))
    for obj in remain_objects:
        print(obj)

if __name__ == "__main__":
    main()