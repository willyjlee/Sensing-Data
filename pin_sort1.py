import sys

def ispin(str):# str is string                                                                                 
    if len(str)<=1:
        return False
    str = str.strip("\"")
    if len(str)<=1:
        return False
    if str[0]!='P':
        return False
    rem = str[1:]
    return rem.isdigit()

def pincmp(x, y):#receives ispin==true 
    ox = x
    oy = y
    x =x.strip("\"")
    y =y.strip("\"")
    x=x[1:]
    y=y[1:]
    x=int(x)
    y=int(y)
    if x>y:
#        print(ox + ' > ' + oy)
        return 1
    elif x<y:
 #       print(ox+ ' < '+ oy)
        return -1
    else:
  #      print(ox+ ' == '+ oy)
        return 0

if len(sys.argv)!=2:
    print("wrong format")
    sys.exit(1)

fn = sys.argv[1]

fd = open(fn, 'r')
lines = fd.readlines()
fd.close()

fd = open(sys.argv[1]+'.out','w')

for line in lines:
    line = line.split(',')

    for i in range(len(line)):
        word = line[i].rstrip('\n')
#        print(word)
        if ispin(word) or (i-1>=0 and ispin(line[i-1])==True):
            continue
        fd.write(word + ',')
    
    d=dict()
    pins=[]
    for i in range(len(line)):
        word = line[i].rstrip('\n')
        if ispin(word):
            print("pin")
            if i+1==len(line):
                print("no v for pin")
                sys.exit(1)
            d[word]=line[i+1].rstrip('\n')
            pins.append(word)

    print("hi")
    pins = sorted(pins, cmp = pincmp)
    print(pins)
    
    for i in range(len(pins)):
        pin = pins[i]
        fd.write(pin+',')
        fd.write(d[pin])
        if i!=len(pins)-1:
            fd.write(',')
    
    fd.write('\n')

fd.close()

print('good')
