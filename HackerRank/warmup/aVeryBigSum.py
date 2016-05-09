# Author: Enes Kemal Ergin
# Date: 05/09/16
# https://www.hackerrank.com/challenges/a-very-big-sum

a = int(raw_input())
b = raw_input()

num_b = [int(i) for i in b.split(" ")]

print sum(num_b)


# Efficient Solution from someone else
input()
print(sum(map(int, input().split())))
