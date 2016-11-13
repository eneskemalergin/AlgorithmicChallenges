# Author: Enes Kemal Ergin
# Date: 11/13/16
# https://www.hackerrank.com/challenges/circular-array-rotation

# n -> number of intergers in list
# k -> times of operation performed
# m -> number of printing cases
n, k, m = map(int, raw_input().strip().split())

# Get the list of integers and store it in arr
arr = list(map(int, raw_input().strip().split()))

# Iterate m times
for _ in range(m):
    # Get the index of number
    idx = int(raw_input())
    # Print the value in given index
    print(arr[(idx - k) % n])
