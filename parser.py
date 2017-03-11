import json

file_name = 'data_pins.txt'

def append_pair(key, value):
  s = ''
  if type(value) is dict:
    for k in value:
    	s = append_pair(k, value[k]) + s
  else:
    key_str = ''
    value_str = ''

    if str(key).isdigit():
      key_str = str(key)
    else:
      key_str = '"' + str(key) + '"'

    if str(value).isdigit():
      value_str = str(value)
    else:
      value_str = '"' + str(value) + '"'
    s = key_str + ',' + value_str + ','

  return s
def dict_to_csv(d):
  s = ''
  if type(d) is not dict:
    return s
  else:
    for k in d:
      s = append_pair(k, d[k]) + s
  s = s[:-1]
  return s

lc_fd = open(file_name, 'r')
lines = lc_fd.readlines()
lc_fd.close()

parsed = []
for line in lines:
  try:
    parsed.append(json.loads(line.replace('"{', '{').replace('}"', '}')))
  except:
  	pass
text = []
for line in parsed:
  text.append(dict_to_csv(line))

out_fd = open(file_name.rstrip('.txt') + '_csv.txt', 'w')
for s in text:
  out_fd.write(s + '\n')
out_fd.close()
