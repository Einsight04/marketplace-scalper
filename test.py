import re

message = 'item.c: Iphone 12 [mini]'

qlist = re.findall("[]",message)

print(qlist)