# Author: Enes Kemal Ergin
# Date: 05/13/16
# https://www.hackerrank.com/challenges/manasa-and-stones

for i in range(input()):
    steps = []
    n = input()
    a = input()
    b = input()
    a, b = min(a, b), max(a, b)
    minn = (n - 1) * a
    for i in range(0, n):
        step = minn - a * i + b * i
        if step not in steps:
            steps.append(step)
    print ' '.join(map(str, steps))
