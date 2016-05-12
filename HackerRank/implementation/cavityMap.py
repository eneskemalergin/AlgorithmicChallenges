# Author: Enes Kemal Ergin
# Date: 05/12/16
# https://www.hackerrank.com/challenges/cavity-map

n=input()
b=[]
for i in xrange(n):
	a=raw_input().strip()
	c=map(int,list(a))
	b.append(c)
for i in xrange(n):
	for j in xrange(n):
		if i!= 0 and j != 0 and i != n-1 and j != n-1:
			if b[i-1][j]< b[i][j] and b[i][j-1]< b[i][j] and b[i+1][j]< b[i][j] and b[i][j+1]< b[i][j]:
				b[i][j]='X'
for i in xrange(n):
	c=map(str , b[i])
	print ''.join(c)
