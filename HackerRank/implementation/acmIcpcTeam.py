# Author: Enes Kemal Ergin
# Date: 05/13/16
# https://www.hackerrank.com/challenges/acm-icpc-team

N,k=map(int,raw_input().split())
l=[]
for i in xrange(N):
    l.append(int(raw_input(),2))
maxtopics=-1
nummax=1
for i in xrange(N):
    for j in xrange(i+1,N):
        topics=len([k for k in bin(l[i]|l[j]) if k=='1'])
        if(topics>maxtopics):
            nummax=1
            maxtopics=topics
        elif(topics==maxtopics):
            nummax+=1
print maxtopics
print nummax
