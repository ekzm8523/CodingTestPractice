#https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    """
    :param lottos: 로또 번호를 담은 배열
    :param win_nums: 당첨 번호를 담은 배열
    :return: 당첨 가능한 최고순위, 최저순
    """
    rank = [6, 6, 5, 4, 3, 2, 1]
    best = worst = 0

    for lotto in lottos:
        if lotto == 0:
            best += 1
        if lotto in win_nums:
            best += 1
            worst += 1

    return [rank[best], rank[worst]]

if __name__ == "__main__":

    lottos1 = [44, 1, 0, 0, 31, 25]
    lottos2 = [0, 0, 0, 0, 0, 0]
    lottos3 = [45, 4, 35, 20, 3, 9]

    win_nums1 = [31, 10, 45, 1, 6, 19]
    win_nums2 = [38, 19, 20, 40, 15, 25]
    win_nums3 = [20, 9, 3, 45, 4, 35]

    print(solution(lottos1, win_nums1))     # [3, 5]
    print(solution(lottos2, win_nums2))     # [1, 6]
    print(solution(lottos3, win_nums3))     # [1, 1]