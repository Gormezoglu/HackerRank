import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    pair=0
    if (1<n<100):
        if (len(ar)<=n):
            sorted_ar = sorted(ar)
            l_unique = list(set(sorted_ar))
            countDict = {i:sorted_ar.count(i) for i in l_unique}
            for k,v in countDict.items():
                pair += v//2        
        else:
            raise ValueError ('Array length exceeds the max limit')        
    else:
        raise ValueError ('n must be between 1 and 100')    
    
    return pair

sockMerchant(100, [42]*100)

