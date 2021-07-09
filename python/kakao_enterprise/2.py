#
# """
# IPv4
# - A.B.C.D로 구성, 모든 A,B,C,D의 len은 3을 넘어선 안된다.
# - 0~255 범위의 10진 정수이다.
# - 앞에 0이 있으면 뒤에 숫자가 8이상이면 안된다.
# - 앞이나 뒤에 .으로 시작하면 안된다. 즉 A.B.C.D의 포멧을 지켜야
#
# IPv6
# - A:B:C:D:E:F:G:H 꼴로 생겼고 각각의 그룹은 4자리의 16진수로 구성
# - 앞에 선행 0을 지울 수 있다. 그러나 앞에는 지우고 뒤에는 안지우고 안됨 -> 이게 함정인듯
# - 연속되는 0 섹션은 이중 콜론 (::)으로 대체 가능 그러나 한번만 쓸 수 있다.
# """
# def isIPv6(address):
#
#
#     if address.find("::") != -1: # 축약버전
#         if address.count("::") > 2:
#             print("::이 두개에요")
#             return False
#         if address.find(":::") != -1:
#             print(":::은 뭐죠?")
#             return False
#         if address.find("::") == 0:
#             address = address.replace('::', '')
#         else:
#             address = address.replace('::', ':')
#
#         add = address.split(":")
#         for value in add:
#             for i in value:
#                 if not (i.isdigit() or 'a' <= i <= 'f'):
#                     print("index에 16진수가 아닌게 있음")
#                     return False
#     else: # 축약 안했을때
#         if address.count(":") != 7:
#             print(":의 갯수가 7이 아님")
#             return False
#         add = address.split(":")
#         zero_flag = False
#
#         for value in add:
#             if len(value) < 4:
#                 zero_flag = True
#             if zero_flag and len(value) > 1 and value[0] == '0':
#                 print("0축약을 하기로 했으면서 왜안해용?")
#                 return False
#
#             for i in value:
#                 if not (i.isdigit() or 'a' <= i <= 'f'):
#                     print("index에 16진수가 아닌게 있음")
#                     return False
#     return True
#
# def isIPv4(address):
#     if address.count('.') != 3:
#         print(".의 갯수가 3이 아님")
#         return False
#     add = address.split('.')
#
#     for value in add:
#         if len(value) > 3 or len(value) == 0:
#             print("길이 오류")
#             return False
#         if int(value) < 0 or int(value) > 255:
#             print("0~255가 아님")
#             return False
#         if value[0] == '0' and int(value) > 8:
#             print("0으로 시작할때 8이 넘으면 안됨")
#             return False
#     return True
#
#
#
#
# def solution(addresses):
#
#     for address in addresses:
#         print(address)
#         if isIPv4(address):
#             print("IPv4")
#         elif isIPv6(address):
#             print("IPv6")
#         else:
#             print("Neither")
#
#
# if __name__ == "__main__":
#     ex_list = ['121.18.19.20', '0.12.12.34', '121.234.12.12', '23.45.12.56', '0.1.2.3']
#     solution(ex_list)
#     ex_list = ['2001::db8:0000:0000:0000:ff00:0042:8329', '2001:db8:0:0:0:ff00:42:8329', '2001:db8::ff00:42:8329',
#      '0000:0000:0000:0000:0000:0000:0000:0001', '::1']
#     solution(ex_list)
#     ex_list = ['000.012.234.23', '666.666.23.23', '.213.123.23.32',
#                '23.45.22.32.', '272:2624:235e:3bc2:c46d:682:5d46:638g', '1:22:333:4444']
#     print(solution(ex_list))

# !/bin/python

import math
import os
import random
import re
import sys


#
# Complete the 'validateAddresses' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY addresses as parameter.
#
def isIPv6(address):
    if address.find("::") != -1:  # 축약버전
        if address.count("::") > 2:  # ::은 한번만 쓸 수 있음
            return False
        if address.find(":::") != -1:  # :::인경우 제거
            return False
        if address.find("::") == 0:
            address = address.replace("::", '')  # ::으로 시작한다면 없애주고
        else:
            address = address.replace("::", ':')  # ::이 중간에 있다면 :으로 변경해주기

        add = address.split(":")
        zero_flag = False

        for value in add:
            if len(value) < 4:  # 4자리가 아니라면 앞에 0을 생략했다는 것 zero_flag 활성화
                zero_flag = True
            if zero_flag and len(value) > 1 and value[0] == "0":  # zero_flag가 활성화 되었는데 0으로 시작하면 안됨
                return False
            for i in value:
                if not (i.isdigit() or 'a' <= i <= 'f'):  # 16진수인지 확인
                    return False


    else:  # 축약 안했을 때
        if address.count(":") != 7:  # 기본 틀에 맞지 않음
            return False
        add = address.split(":")
        zero_flag = False

        for value in add:
            if len(value) < 4:  # 4자리가 아니라면 앞에 0을 생략했다는 것 zero_flag 활성화
                zero_flag = True
            if zero_flag and len(value) > 1 and value[0] == "0":  # zero_flag가 활성화 되었는데 0으로 시작하면 안됨
                return False
            for i in value:
                if not (i.isdigit() or 'a' <= i <= 'f'):  # 16진수인지 확인
                    return False
    return True


def isIPv4(address):
    if address.count('.') != 3:  # .의 갯수가 3이 아님
        return False
    add = address.split('.')

    for value in add:
        if len(value) > 3 or len(value) == 0:  # 4자리가 넘거나 아무것도 안써져있는 오류 제거 -> 맨앞 맨뒤에 .이 있는경우도 이에 포함
            return False
        if int(value) < 0 or int(value) > 255:  # out of range
            return False
        if value[0] == '0' and int(value) > 8:  # 0으로 시작할때 8이 넘으면 안됨
            return False
    return True


def validateAddresses(addresses):
    answer = []
    for address in addresses:
        if isIPv4(address):
            answer.append('IPv4')
        elif isIPv6(address):
            answer.append("IPv6")
        else:
            answer.append("Neither")

    return answer


if __name__ == '__main__':
    pass