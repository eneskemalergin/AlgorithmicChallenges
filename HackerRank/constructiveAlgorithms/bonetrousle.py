# Author: Enes Kemal Ergin
# Date: 11/26/16
# https://www.hackerrank.com/challenges/bonetrousle

t=input()
for _ in range(t):
    [n,k,b]=map(int,raw_input().strip().split())
    v0=b*(b+1)/2
    if n<v0:
        print -1
    else:
        s=(n-v0)/b
        r=(n-v0)%b
        if s > k-b:
            print -1
        elif s == k-b and r > 0:
            print -1
        else:
            a=range(s+1,s+b+2)
            del a[b-r]
            print ' '.join(map(str,a))
