# Author: Enes Kemal Ergin
# Date: 05/11/16
# https://www.hackerrank.com/challenges/service-lane

import math
n, t = map(int, raw_input().split())
width = map(int, raw_input().split())
for i in range(t):
	x,y = map(int, raw_input().split())
	min_value = min(width[x:(y+1)])
	print min_value
