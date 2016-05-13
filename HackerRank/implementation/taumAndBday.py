# Author: Enes Kemal Ergin
# Date: 05/13/16
# https://www.hackerrank.com/challenges/taum-and-bday

t=int(input())
for i in range(t):
    temp=raw_input()
    black,white=temp.split()

    black=int(black)
    white=int(white)

    temp=raw_input()
    x,y,z=temp.split()

    x=int(x)
    y=int(y)
    z=int(z)

    print(min(black*x + white*y,(black+white)*x + z*white,(black+white)*y + z*black))
