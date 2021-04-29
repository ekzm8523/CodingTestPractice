from collections import deque

def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        dif = 0
        for c, w in zip(current, word):
            if c != w:
                dif += 1
        if dif == 1:
            yield word

def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)
    print(dist)
    return dist.get(target, 0)

if __name__ == "__main__":
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(begin, target, words))