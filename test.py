# 숫자 몇까지 고정된 주솟값을 가질까?
# if __name__ == '__main__':
#     for num in range(10000):
#         num_address = id(num)
#         for _ in range(10):
#             new_num_address = num + num - num
#             if id(new_num_address) != num_address:
#                 print(num, " 여기부터는 새롭게 할당됩니다.")
#                 exit()


# from threading import Timer
#
#
# if __name__ == '__main__':
#
#     while True:
#         t = Timer(3, print, "time out")
#         t.start()
#         inp = input("3초안에 입력하세요")
#         print(inp)
#         t.cancel()


