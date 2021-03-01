test_n = int(input())

test_size_list = []
test_list = []
real_list = []
b = []

for i in range(test_n):
    n,m = map(int,input().split())
    _list = list(map(int,input().split()))
    test_size_list.append((n,m))
    test_list.append(_list)
    slice_index = 0
    a = []
    for j in range(n):
        a.append(_list[slice_index:slice_index+m])
        slice_index += m
    b.append(a)
test_list = b

for epoch in range(test_n):
    matrix = test_list[epoch]
    n,m = test_size_list[epoch]
    print("---------------")
    print(matrix)
    for i in range(1,m):
        for j in range(n):
            if j == 0:
                matrix[j][i] += max(matrix[j][i-1],matrix[j+1][i-1])
            elif j+1 == n:
                matrix[j][i] += max(matrix[j-1][i-1],matrix[j][i-1])
            else:
                matrix[j][i] += max(matrix[j-1][i-1],matrix[j+1][i-1],matrix[j][i-1])
    print(max(a[m-1] for a in matrix))





    





