# Author: Enes Kemal Ergin
# Date: 05/11/16
# https://www.hackerrank.com/challenges/plus-minus

n = int(raw_input())

a = map(int, raw_input().split())

zeroes = 0
negative = 0
positive = 0

for i in xrange(n):
    if (a[i] == 0):
        zeroes += 1
    elif (a[i] < 0):
        negative += 1
    else:
        positive += 1

print 1.0 * positive / n
print 1.0 * negative / n
print 1.0 * zeroes / n
