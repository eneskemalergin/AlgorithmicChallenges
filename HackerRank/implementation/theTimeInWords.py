# Author: Enes Kemal Ergin
# Date: 05/13/16
# https://www.hackerrank.com/challenges/the-time-in-words

numbers_words={0:"o'clock", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven",
       8:"eight",9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen",
       14:"fourteen", 15:"quarter", 16:"sixteen", 17:"seventeen", 18:"eighteen",
       19:"nineteen", 20:"twenty", 21:"twenty one", 22:"twenty two", 23:"twenty three",
       24:"twenty four", 25:"twenty five", 26:"twenty six", 27:"twenty seven",
       28:"twenty eight", 29:"twenty nine", 30:"half"}
H = int(raw_input())
M = int(raw_input())
if H > 12:
    H = H - 12
in_str = ""

if M == 0:
    in_str = numbers_words[H] + " o' clock"
elif M < 31:
    if M == 1:
        in_str = numbers_words[M] + " minute past " + numbers_words[H]
    elif M == 15 or M == 30:
        in_str = numbers_words[M] + " past " + numbers_words[H]
    else:
        in_str = numbers_words[M] + " minutes past " + numbers_words[H]
else:
    M = 60 - M
    if H == 12:
        H = 0
    if M == 1:
        in_str = numbers_words[M] + " minute to " + numbers_words[H+1]
    elif M == 15 :
        in_str = numbers_words[M] + " to " + numbers_words[H+1]
    else:
        in_str = numbers_words[M] + " minutes to " + numbers_words[H+1]

print(in_str)
