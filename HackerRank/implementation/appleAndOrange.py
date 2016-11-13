# Author: Enes Kemal Ergin
# Date: 11/13/16
# https://www.hackerrank.com/challenges/apple-and-orange


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

nb = 0
for ap in apple:
    if (a+ap) >= s and (a+ap) <= t:
        nb += 1
print(nb)

nb = 0
for org in orange:
    if (b+org) >= s and (b+org) <= t:
        nb += 1
print(nb)
