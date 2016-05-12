# Author: Enes Kemal Ergin
# Date: 05/11/16
# https://www.hackerrank.com/challenges/cut-the-sticks

nSticks = int(raw_input())
stickLengths = [int(x) for x in raw_input().split()]
cuts = 0
totalCutLength = 0
stickLengths = sorted(stickLengths)
i = 0
while i < len(stickLengths):
    print len(stickLengths)-i
    totalCutLength = stickLengths[i]
    while i < len(stickLengths) and stickLengths[i] <= totalCutLength:
        i += 1
