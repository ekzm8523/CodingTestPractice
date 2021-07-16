# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxTickets function below.
def maxTickets(tickets):
    tickets.sort()
    answer = 0
    tmp = 1
    for i in range(tickets_count - 1):
        if tickets[i] + 1 >= tickets[i + 1]:
            tmp += 1
        else:
            if tmp > answer:
                answer = tmp
            tmp = 1

    return answer


if __name__ == '__main__':
    tickets_count = 4
    tickets = [4, 13, 2, 3]
    print(maxTickets(tickets))
