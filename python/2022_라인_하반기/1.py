import math
from typing import List


def solution(queries: List[List[int]]) -> int:
    answer = 0

    size_dict = {}

    for array_num, cnt in queries:
        if array_num not in size_dict:
            size_dict[array_num] = [cnt, 2 ** math.ceil(math.log2(cnt))]
        else:
            required_size = cnt + size_dict[array_num][0]
            if required_size <= size_dict[array_num][1]:
                size_dict[array_num][0] = required_size
            else:  # 복사
                size_dict[array_num][1] = 2 ** math.ceil(math.log2(required_size))
                answer += size_dict[array_num][0]
                size_dict[array_num][0] = required_size

    return answer


if __name__ == '__main__':
    print(solution([[2, 10], [7, 1], [2, 5], [2, 9], [7, 32]]))
    print(solution([[1, 1], [1, 2], [1, 4], [1, 8]]))


