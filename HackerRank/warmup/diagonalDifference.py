# Author: Enes Kemal Ergin
# Date: 05/10/16
# https://www.hackerrank.com/challenges/diagonal-difference

n = int(raw_input())

rows = []

for i in xrange(n):
     row = map(int, raw_input().split())
     rows.append(row)

diagonal_1 = 0
diagonal_2 = 0

for i in xrange(n):
    diagonal_1 += rows[i][i]
    diagonal_2 += rows[i][n - i - 1]

print abs(diagonal_2 - diagonal_1)
