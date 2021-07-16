#!/bin/python3

import math
import os
import random
import re
import sys


def getMinDeletions(s):
    # Write your code here
    dist_count = 0
    count = [0] * 26

    for ch in s:
        if count[ord(ch) - ord('a')] == 0:
            dist_count += 1
        count[ord(ch) - ord('a')] += 1
    return len(s) - dist_count


if __name__ == '__main__':
    s = "abcab"
    print(getMinDeletions(s))