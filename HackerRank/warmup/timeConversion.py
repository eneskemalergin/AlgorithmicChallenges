# Author: Enes Kemal Ergin
# Date: 05/11/16
# https://www.hackerrank.com/challenges/time-conversion

def to_time_part(value):
    if (value < 10):
        return '0' + str(value)
    else:
        return str(value)

line = raw_input()

parts = line.split(':')

hh = int(parts[0])
mm = int(parts[1])
ss = int(parts[2][:2])
isAmTime = parts[2][2:] == "AM"

if (hh == 12 and mm == 0 and ss ==0):
    if (isAmTime):
        print "00:00:00"
    else:
        print "12:00:00"
else:
    if isAmTime :
        if hh < 12:
            print to_time_part(hh) + ":" + to_time_part(mm) + ":" + to_time_part(ss)
        else:
            print to_time_part(hh - 12) + ":" + to_time_part(mm) + ":" + to_time_part(ss)
    else:
        if hh < 12:
            print to_time_part(hh + 12) + ":" + to_time_part(mm) + ":" + to_time_part(ss)
        else:
            print to_time_part(hh) + ":" + to_time_part(mm) + ":" + to_time_part(ss)

