# Author: Enes Kemal Ergin
# Date: 05/12/16
# https://www.hackerrank.com/challenges/caesar-cipher-1

n = input()
s = raw_input()
k = input()
output = list(s)
k %= (ord('z') - ord('a') + 1)

for idx, l in enumerate(output):
    if l.isalpha():
        if l.isupper():
            new_char = ord(l)+k
            if new_char > ord('Z'):
                new_char = new_char - ord('Z') + ord('A') - 1
            output[idx] = chr(new_char)
        else:
            new_char = ord(l)+k
            if new_char > ord('z'):
                new_char = new_char - ord('z') + ord('a') - 1
            output[idx] = chr(new_char)
return ''.join(output)
