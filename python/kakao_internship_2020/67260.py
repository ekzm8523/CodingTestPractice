"""
사이클 X
위상정렬 사용
위상정렬이란 어떤 노드를 접근하기 전에 먼저 방문해야하는 노드가 있을때 순서를 정해주는 알고리즘이다.
자식에 접근하려면 어차피 부모 노드를 거쳐야 한다.
무방향 그래프에서 부모에서 자식을 가리키는 방향 그래프로 변경
그리고 order에 있는 먼저 거쳐야 하는 순서도 (A, B) 라고 치면 B의 injection_node 에 추가해준다.

1. 무방향 그래프에서 부모에서 자식을 가리키는 방향 그래프로 변경
2. 들어오는 노드, 나가는 노드 그래프를 만들고 order도 A -> B 간선으로 추가해준다.
3. 위상정렬을 실행한다.
4. 본문에서는 사이클은 발생하지 않는다는 가정이 있었지만 order 를 추가해줌으로써 사이클이 발생할 수 있다.
5. 사이클 판별 하고 전체 순회를 했을때 모든 노드를 방문 했으면 return True else return False
"""
from collections import deque

def solution(n, path, order):

    undirected_graph = {i: [] for i in range(n)}    # 무방향 그래프
    for a, b in path:
        undirected_graph[a].append(b)
        undirected_graph[b].append(a)

    injection_node = {i: [] for i in range(n)}  # 각 노드에 들어오기 전에 선행되어야 될 노드를 기록
    directed_graph = {i: [] for i in range(n)}  # 방향 그래프 ( 부모에서 자식 방향 )
    visit_set = set()
    q = deque((0,))

    while q:
        node = q.popleft()  # 방문 노드
        visit_set.add(node)     # 기록

        for next_node in undirected_graph[node]:    # 그 노드에서 접근할 수 있는 모든 노드를 가져온다 ( 자식노드 + 부모노드 전부 가져옴 )
            if next_node not in visit_set:  # 만약 그 노드가 방문하지 않은 노드라면 (자식 노드라면)
                q.append(next_node)     # queue 에 넣어주고 (다음 방문 순위)
                injection_node[next_node].append(node)  # 자식노드 입장에서는 부모노드가 선행 되어야 함
                directed_graph[node].append(next_node)  # 그래프 개념에서는 부모에서 자식을 가리키는게 맞음

    for k in range(n):
        del undirected_graph[k]  # dict.clear() 를 해도 된다고 한다. C언어 뽐뿌와서 해봄
    del undirected_graph    # 얘는 이제 쓸모 없음 방향 그래프와 인접노드 dict 만 사용할거임

    for a, b in order:  # 선행되어야 할 노드 ( A -> B )
        injection_node[b].append(a)    # B 입장에서 A가 선행되어야 함 ( 어차피 밑에서 set으로 중복 제거 해줄 것 이기 때문에 밑에처럼 필터링X)
        if b not in directed_graph[a]:  # A의 입장에서 B가 자식이 되는건데 이미 자식으로 되어 있었다면 또 추가해줄 필요가 없음
            directed_graph[a].append(b)

    # 중복제거와 delete 의 빈번함 때문에 set 으로 변경  ( list 의 del -> O(index) , set 의 del -> O(1) )
    # 그리고 지우고 매번 length 를 비교해봐야 하기 때문에 set 으로 하는게 맞다. ( len(list) -> O(n) , len(set) -> O(1) )
    for k, v in injection_node.items():
        if v:
            injection_node[k] = set(v)

    print(f"directed_graph -> {directed_graph}")
    print(f"injection_node -> {injection_node}")
    q2 = deque((0,))
    visit_set = set()
    while q2:
        node = q2.popleft()  # node in parent

        for next_node in directed_graph[node]:  # next node is child
            if next_node in visit_set:  # cycle 판별 : 이미 방문했는데 또 자식으로 있음
                return False
            injection_node[next_node].remove(node)  # 방문 처리한 노드는 injection 을 끊어야 함 ( 위상정렬 알고리즘 base )
            if len(injection_node[next_node]) == 0:  # 연결을 끊었을때 들어오는 노드가 없다면 queue에 넣기
                del(injection_node[next_node])  # 들어오는 노드가 없으므로 이제 쓸모가 없음
                q2.append(next_node)

        visit_set.add(node)  # 위에 cycle 판별을 넘어 가고 모든 연결을 끊고나서 set 에 추가
        print(f"remove {node}")

    return len(visit_set) == n


if __name__ == '__main__':
    n = 9
    path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
    order = [[8,5],[6,7],[4,1]]
    print(solution(n, path, order))

    n = 9
    path = [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]]
    order = [[4,1],[5,2]]
    print(solution(n, path, order))

    n = 9
    path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
    order = [[4,1],[8,7],[6,5]]
    print(solution(n, path, order))

    n = 3
    path = [[0, 1], [1, 2]]
    order = [[2, 1]]
    print(solution(n, path, order))