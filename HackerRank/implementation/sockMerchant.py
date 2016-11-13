# Author: Enes Kemal Ergin
# Date: 11/13/16
# https://www.hackerrank.com/challenges/sock-merchant

n=int(raw_input().strip())
arr=map(int,raw_input().strip().split())

count=[0]*101
for c in arr:
    count[c]+=1
out = 0
for i in range(1,101):
    out += count[i]/2
print out
