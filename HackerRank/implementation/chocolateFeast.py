# Author: Enes Kemal Ergin
# Date: 05/11/16
# https://www.hackerrank.com/challenges/chocolate-feast

for i in range (input()):
    A,B,C = map(int, raw_input().split())
    wrappers = A / B
    total = wrappers
    while C <= wrappers:
        count = wrappers / C
        total += count
        wrappers = (wrappers % C) + count
    print total
