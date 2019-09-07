#convert json to python 

import json

fh = open('text.json','r')
data= fh.read()
fh.close()

print(type(data))

print(json.loads(data))
print(type(json.loads(data)))
