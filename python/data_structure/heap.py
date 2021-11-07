import heapq

def heapsort(iterable):
    heap = []
    for value in iterable:
        heapq.heappush(heap, value)

    sorted_list = []
    while heap:
        sorted_list.append(heapq.heappop(heap))

    return sorted_list

if __name__ == '__main__':
    l = [4,2,5,1,7,3,6,9,8]
    print(heapsort(l))