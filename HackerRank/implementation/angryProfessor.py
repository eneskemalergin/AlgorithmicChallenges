# Author: Enes Kemal Ergin
# Date: 05/11/16
# https://www.hackerrank.com/challenges/angry-professor

t = int(raw_input())
for _ in xrange(t):
    n, k = map(int, raw_input().split())

    arr = map(int, raw_input().split())
    for i in arr:
        if i <= 0:
            k -= 1
        if k == 0:
            print 'NO'
            break
    else:
        print 'YES'
