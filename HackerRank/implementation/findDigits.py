# Author: Enes Kemal Ergin
# Date: 05/11/16
# https://www.hackerrank.com/challenges/find-digits

T = input()
for i in range(T):
    N = raw_input()
    count = 0
    for digit in N:
        if digit != '0' and int(N) % int(digit) == 0:
            count = count + 1
    print count
