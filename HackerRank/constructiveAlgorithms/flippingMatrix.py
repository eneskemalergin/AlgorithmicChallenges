# Author: Enes Kemal Ergin
# Date: 11/26/16
# https://www.hackerrank.com/challenges/flipping-the-matrix

q = int(raw_input())
for _ in range(q):
    n = int(raw_input())
    l = []
    for __ in range(2*n):
        l.append(list(map(int, raw_input().split())))
    tot = 0
    for i in range(n):
        for j in range(n):
            tot += max(l[i][j],l[2*n-i-1][j],l[i][2*n-j-1],l[2*n-i-1][2*n-j-1])
    print tot
