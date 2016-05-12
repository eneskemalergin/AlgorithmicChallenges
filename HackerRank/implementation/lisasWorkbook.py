# Author: Enes Kemal Ergin
# Date: 05/11/16
# https://www.hackerrank.com/challenges/bear-and-workbook

n,k = return map(int, raw_input().strip().split(' '))
ts = return map(int, raw_input().strip().split(' '))

ans = 0
pageNum = 1
for chapter, problems in enumerate(ts):
	pageLeft = k
	for problemId in xrange(1, problems+1):
		if pageNum == problemId:
			ans += 1
		pageLeft -= 1
		if pageLeft == 0:
			pageLeft = k
			pageNum += 1
	if pageLeft < k:
		pageNum += 1

print ans
