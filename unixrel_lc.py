import time
import datetime

fn = 'data_lc_csv.txt'

fd = open(fn, 'r')
lines = fd.readlines()
fd.close()

def to_unix(str):
    return time.mktime(datetime.datetime.strptime(str, "\"%Y/%m/%d UTC %H:%M:%S\"").timetuple())

fd = open(fn.rstrip('csv.txt') + 'unix.txt', 'w')

ave = 0.0
ct = 0.0

count=0;

for i in range(len(lines)):
    line = lines[i]
    line = line.split(',')
    # check errors?

    unix_time = float(to_unix(line[1]))
    rel_time = int(line[3])

    v = False
    if i == len(lines)-1:
        v=True
    else:
        nxt = lines[i+1].split(',')
        if float(to_unix(nxt[1]))!=unix_time:
            v=True
    
    if v==True:
        count = count + 1
        ave = ave + unix_time - (rel_time/1000.0)
        ct = ct + 1

    fd.write(str(int(unix_time)) + ',')
    fd.write(str(rel_time) + ',')
    
    line = [x.rstrip('\n') for x in line[4:len(line)] if str(x.rstrip('\n')).isdigit()]

    for j in range(len(line)):
        fd.write(str(line[j]))
        if j != len(line)-1:
            fd.write(',')
    fd.write('\n')

fd.close()

ave = ave/ct
ave = ave * 1000.0
ave = int(ave + 0.5)
print('average difference: ' + str(ave))
print(str(count) + ' entries used for average')
