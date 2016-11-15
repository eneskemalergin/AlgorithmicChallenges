# Author: Enes Kemal Ergin
# Date: 11/15/16
# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies


i,j,k = map(int, raw_input().strip().split(" "))


counter = 0

for _ in range(j-i+1):
    value = (i + _)
    new_value = abs(value - int(str(value)[::-1])) / float(k)
    print new_value
    if new_value.is_integer():
        counter += 1

print counter
