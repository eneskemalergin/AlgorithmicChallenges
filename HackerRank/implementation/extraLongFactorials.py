# Author: Enes Kemal Ergin
# Date: 05/13/16
# https://www.hackerrank.com/challenges/extra-long-factorials

n = int(raw_input());

ret = 1;
for i in range(1, n + 1):
    ret *= i
print ret
