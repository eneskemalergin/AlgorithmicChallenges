# Author: Enes Kemal Ergin
# Date: 05/11/16
# https://www.hackerrank.com/challenges/sherlock-and-the-beast

# Python v3

T=int(input())

K=[int(input()) for i in range(T)]

for k in K:
  for x in range(k//3,-1,-1):
    if (k-3*x)%5==0:
      y=(k-3*x)//5
      print('5'*3*x+'3'*5*y)
      break
    elif x==0:
      print(-1)
