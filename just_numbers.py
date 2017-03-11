fn = 'data_pins_csv.txt'

fd = open(fn, 'r')
lines = fd.readlines()
fd.close()

fd = open(fn.rstrip('csv.txt') + 'num.txt', 'w')

for line in lines:
  line = [x.rstrip('\n') for x in line.split(',') if str(x.rstrip('\n')).isdigit()]
  for word in line:
    fd.write(str(word) + ' ')
  fd.write('\n')
     
fd.close()
