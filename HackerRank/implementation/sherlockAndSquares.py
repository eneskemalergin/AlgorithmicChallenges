# Author: Enes Kemal Ergin
# Date: 05/11/16
# https://www.hackerrank.com/challenges/sherlock-and-squares

from math import sqrt, floor, ceil

square = sqrt
fl = floor
ce = ceil
T = int(raw_input())
for _ in xrange(T):
    (a, b) = map(int, raw_input().split())
    print int(fl(square(b)) - ce(square(a)) + 1)
