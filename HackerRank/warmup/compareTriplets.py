# Author: Enes Kemal Ergin
# Date: 10/12/16
# https://www.hackerrank.com/challenges/compare-the-triplets

a = map(int,(raw_input().strip().split(' ')))
b = map(int,(raw_input().strip().split(' ')))

scoreA = 0
scoreB = 0

for i in range(len(a)):
    if a[i] > b[i]:
        scoreA += 1
    elif a[i] < b[i]:
        scoreB += 1
    else:
        continue

print scoreA, scoreB
