# Author: Enes Kemal Ergin
# Date: 05/16/16
# https://www.hackerrank.com/challenges/matrix-rotation-algo

def iterate_circle(mat, m, n, i):
    for j in xrange(i, m - i - 1):
        yield (j, i)
    for j in xrange(i, n - i - 1):
        yield (m - i - 1, j)
    for j in xrange(m - i - 1, i, -1):
        yield (j, n - i - 1)
    for j in xrange(n - i - 1, i, -1):
        yield (i, j)

def rotate(mat, m, n, r):
    for i in xrange(min(m, n) / 2):
        circle_length = 2 * (m + n - 4 * i) - 4
        offset = circle_length - (r % circle_length)
        if offset == circle_length:
            continue
        line = [mat[x][y] for (x, y) in iterate_circle(mat, m, n, i)]
        for (x, y) in iterate_circle(mat, m, n, i):
            mat[x][y] = line[offset]
            offset = (offset + 1) % circle_length


[m, n, r] = [int(s) for s in raw_input().split(' ')]
mat = [[0 for j in xrange(n)] for i in xrange(m)]
for i in xrange(m):
    for (j, s) in enumerate(raw_input().split(' ')):
        mat[i][j] = int(s)
rotate(mat, m, n, r)
for i in xrange(m):
    for j in xrange(n):
        print mat[i][j],
    print ''
