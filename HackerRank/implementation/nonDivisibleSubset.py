# Author: Enes Kemal Ergin
# Date: 11/13/16
# https://www.hackerrank.com/challenges/non-divisible-subset

(n,k) = map(int,raw_input().split())
A = map(int,raw_input().split())

remc = [0] * k
for a in A:
    remc[a%k] += 1

ret = 0
for i in xrange(k):
    if i == 0:
        ret += min(remc[i],1)
        continue

    j = k - i
    if i > j:
        break
    elif i == j:
        ret += min(remc[i],1)
    else:
        ret += max(remc[i],remc[j])

print ret
