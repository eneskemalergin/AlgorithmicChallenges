# Author: Enes Kemal Ergin
# Date: 05/13/16
# https://www.hackerrank.com/challenges/encryption

import math
string = raw_input()
L = len(string)
upperBound = int(math.ceil(math.sqrt(L)))
lowerBound = int(math.floor(math.sqrt(L)))
col = upperBound
row = lowerBound+1 if L > upperBound*lowerBound else lowerBound
ar = []
i = 0
colind = 0
while (i<L):
    ar.append(string[i:i+col])
    colind += 1
    i += col
for i in range(0, col):
    word = ""
    if (i >= L%col) and (L%col != 0):
        row -= 1
    for j in range(0,row):
        word += ar[j][i]
    if (i >= L%col) and (L%col != 0):
        row += 1
    print word,
