# Author: Enes Kemal Ergin
# Date: 11/26/16
# https://www.hackerrank.com/challenges/beautiful-3-set

n = int(raw_input())
k = (2*n/3)+1
print k
b_s = k/2 if k % 2 else k/2 + 1
mod = k if k % 2 else k + 1
for i in range(k):
    b = (b_s + i) % mod
    c = n - i - b
    print i,b,c 
