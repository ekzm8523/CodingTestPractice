import sys


if __name__ == '__main__':

    N, D = map(int, sys.stdin.readline().split())  # N: 이미지 갯수, D: feature 갯수
    bits = [int(x) for x in sys.stdin.readline().split()]  # 각 feature 사이즈들
    image_slicing_size = sum(bits)
    #add code if needed

    raw_data = [int(x, 16) for x in sys.stdin.readline().split()]  #  압축된 데이터
    # binary_data = ''.join([bin(data)[2:][::-1] for data in raw_data])
    #add code if needed

    Q = int(sys.stdin.readline())  # 쿼리 갯수

    for _ in range(Q):
        hamming_distance = []
        image_data = []
        image, range_start, range_end, feature_start, feature_end, K = map(int, sys.stdin.readline().split())
        start_image_bit = (image - 1) * image_slicing_size  # 이미지 1부터 시작
        start_image_row, start_image_col = divmod(start_image_bit, 32)
        feature_start_bit = sum(bits[:feature_start-1])
        feature_end_bit = sum(bits[:feature_end])
        remain_feature_size = feature_end_bit - feature_start_bit
        while remain_feature_size:
            binary_data = f"{bin(raw_data[start_image_row])[2:][::-1]:0<32}"
            if remain_feature_size + start_image_col > 32:
                image_data.append(binary_data[start_image_col:])
                start_image_col = 0
                start_image_row += 1
                remain_feature_size -= (32 - start_image_col)
            else:
                image_data.append(binary_data[start_image_col:start_image_col + remain_feature_size])
                break
        image_data = ''.join(image_data)
        # image_data = binary_data[start_image_bit:start_image_bit + image_slicing_size] \
        #                         [feature_start_bit:feature_end_bit]
        for compare_image in range(range_start, range_end + 1):
            # if compare_image == image:
            #     continue
            compare_image_data = []
            compare_start_image_bit = (compare_image - 1) * image_slicing_size  # 이미지 1부터 시작

            compare_start_image_row, compare_start_image_col = divmod(compare_start_image_bit, 32)
            remain_feature_size = feature_end_bit - feature_start_bit

            while remain_feature_size:
                binary_data = f"{bin(raw_data[compare_start_image_row])[2:][::-1]:0<32}"
                if remain_feature_size + compare_start_image_col > 32:
                    compare_image_data.append(binary_data[compare_start_image_col:])
                    compare_start_image_col = 0
                    compare_start_image_row += 1
                    remain_feature_size -= (32 - compare_start_image_col)
                else:
                    compare_image_data.append(
                        binary_data[compare_start_image_col:compare_start_image_col + remain_feature_size]
                    )
                    break
            compare_image_data = ''.join(compare_image_data)


            # compare_image_data = binary_data[compare_start_image_bit:compare_start_image_bit + image_slicing_size] \
            #                                 [feature_start_bit:feature_end_bit]  # 필요한 특징 벡터만
            h_d = bin(int(image_data, 2) ^ int(compare_image_data, 2)).count('1')

            hamming_distance.append((compare_image, h_d))

        hamming_distance.sort(key=lambda x: (x[1], x[0]))
        print(hamming_distance[K-1][0])
