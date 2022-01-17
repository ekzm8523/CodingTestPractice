import sys
"""
4 2
10 11
e6934fb6 0ec51c1c 000aab55
1
4 2 3 1 2 1
"""


def get_binary_data(image_feature_start_bit: int, image_feature_end_bit: int) -> str:
    global raw_data, bits
    image_data = []

    remain_image_size = image_feature_end_bit - image_feature_start_bit
    image_row, image_col = divmod(image_feature_start_bit, 32)

    while remain_image_size > 0:
        binary_data = f"{bin(raw_data[image_row])[2:][::-1]:0<32}"
        if remain_image_size + image_col > 32:  # 한줄에서 비트 충족이 다 안될때 (다음 라인으로 넘어가야 할 때)
            image_data.append(binary_data[image_col:])
            remain_image_size -= (32 - image_col)
            image_col = 0
            image_row += 1
        else:
            image_data.append(binary_data[image_col:image_col + remain_image_size])
            remain_image_size = 0
    return ''.join(image_data)


if __name__ == '__main__':

    N, D = map(int, sys.stdin.readline().split())
    bits = [int(x) for x in sys.stdin.readline().split()]
    image_slicing_size = sum(bits)

    raw_data = [int(x, 16) for x in sys.stdin.readline().split()]

    Q = int(sys.stdin.readline())
    for _ in range(Q):
        image, range_start, range_end, feature_start, feature_end, K = map(int, sys.stdin.readline().split())
        start_image_bit = (image - 1) * image_slicing_size

        feature_start_bit = sum(bits[:feature_start-1])
        feature_end_bit = sum(bits[:feature_end])
        feature_size = feature_end_bit - feature_start_bit

        image_feature_start_bit = start_image_bit + feature_start_bit
        image_feature_end_bit = start_image_bit + feature_end_bit

        image_data = get_binary_data(image_feature_start_bit, image_feature_end_bit)
        hamming_distance_list = []
        for compare_image in range(range_start, range_end + 1):
            compare_start_image_bit = (compare_image - 1) * image_slicing_size

            compare_image_feature_start_bit = compare_start_image_bit + feature_start_bit
            compare_image_feature_end_bit = compare_start_image_bit + feature_end_bit

            compare_image_data = get_binary_data(compare_image_feature_start_bit, compare_image_feature_end_bit)
            hamming_distance = bin(int(image_data, 2) ^ int(compare_image_data, 2)).count('1')
            hamming_distance_list.append((hamming_distance, compare_image))

        hamming_distance_list.sort(key=lambda x: (x[0], x[1]))
        print(hamming_distance_list[K-1][1])
