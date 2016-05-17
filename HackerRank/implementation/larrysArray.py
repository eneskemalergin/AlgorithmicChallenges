# Author: Enes Kemal Ergin
# Date: 05/16/16
# https://www.hackerrank.com/challenges/larrys-array

t = int(raw_input())
for _ in range(t):
    raw_input()
    n = map(int, raw_input().split())
    inv = 0
    for i in range(len(n) - 1):
        for j in range(i + 1, len(n)):
            if n[i] > n[j]:
                inv += 1
    if inv % 2 == 1:
        print("NO")
    else:
        print("YES")
