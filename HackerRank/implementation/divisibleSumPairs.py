# Author: Enes Kemal Ergin
# Date: 11/13/16
# https://www.hackerrank.com/challenges/divisible-sum-pairs

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))

res = 0
for i in range(n):
    for j in range(i + 1,n):
        if (a[i] + a[j])%k == 0:
            res += 1
print res
