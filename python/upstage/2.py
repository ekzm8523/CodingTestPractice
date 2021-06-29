import heapq

# def find_max_sum(numbers):
#     heap = []
#     for number in numbers:
#         heapq.heappush(heap, -number)
#
#     return -(heapq.heappop(heap) + heapq.heappop(heap))
import sys

def find_max_sum(numbers):
    top1 = top2 = -sys.maxsize

    for number in numbers:
        if top1 < number:
            top2 = top1
            top1 = number
        elif top2 < number:
            top2 = number
    return top1 + top2


if __name__ == "__main__":
    print(find_max_sum([5, 4, 11, 2, 1]))