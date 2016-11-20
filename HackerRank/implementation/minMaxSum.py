# Author: Enes Kemal Ergin
# Date: 05/13/16
# https://www.hackerrank.com/challenges/mini-max-sum

int_list = map(int, raw_input().strip().split(" "))
sum_list = []

for i in int_list:
    sum_list.append((sum(int_list)-i))

print min(sum_list), max(sum_list)
