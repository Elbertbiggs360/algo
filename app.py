import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    search_group = ar
    pairs = []
    for val in search_group:
        key = search_group.pop(search_group.index(val))
        if key in search_group:
            search_group.pop(search_group.index(key))
            pairs.append(key)
    return len(tuple(pairs))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()