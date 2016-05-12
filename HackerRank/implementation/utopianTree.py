# Author: Enes Kemal Ergin
# Date: 05/11/16
# https://www.hackerrank.com/challenges/utopian-tree

for i in range(input()):
    n=input()
    print pow(2,(n+1)/2+1)-1-(n%2)
