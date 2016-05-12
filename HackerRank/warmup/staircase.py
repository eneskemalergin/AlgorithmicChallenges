# Author: Enes Kemal Ergin
# Date: 05/11/16
# https://www.hackerrank.com/challenges/staircase

import sys

n = int(raw_input());

for i in xrange(1, n + 1):
    spaces = n - i
    for j in xrange(spaces):
        sys.stdout.write(' ')
    for j in xrange(i):
        sys.stdout.write('#')
    print
