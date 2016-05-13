# Author: Enes Kemal Ergin
# Date: 05/13/16
# https://www.hackerrank.com/challenges/kaprekar-numbers

import sys

p = int(sys.stdin.readline())
q = int(sys.stdin.readline())

kaprekar = [1, 9, 45, 55, 99, 297, 703, 999, 2223, 2728, 4950, 5050, 7272, 7777, 9999, 17344, 22222, 77778, 82656, 95121, 99999]
ans = [str(k) for k in kaprekar if k>=p and k<=q]
if ans:
    print ' '.join(ans)
else:
    print 'INVALID RANGE'
