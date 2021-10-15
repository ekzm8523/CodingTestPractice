#
# class my_iter(object):
#
#     def __init__(self, _list: list):
#         self.value = _list
#
#     def __iter__(self):
#         self.iter_cnt = -2
#         return self
#
#
#     def __next__(self):
#
#         if self.iter_cnt < len(self.value):
#             yield self.value[self.iter_cnt]
#             self.iter_cnt += 2
#             # return self.value[self.iter_cnt]
#         else:
#             raise StopIteration
#
# if __name__ == '__main__':
#     a = list((1,2,3,4))
#     print(type(a))
#
#     iter_a = my_iter(a)
#     print(type(iter_a))
#
#     for num in iter_a:
#         print(num)

def func(a, **b):
    print(a)
    print(b)


if __name__ == '__main__':
    dic = {'1': 3}
    
    print(*dic)