#scratch data from a website

'''import json
import requests
r = requests.get('http://adv32018.hryssc.in/StaticPages/HomePage.aspx')
data= r.text
new = json.loads(data)
print(new)'''

import requests, json

url = "http://ip-api.com/json"
r_url_with_text = requests.get(url).text

### json
print(r_url_with_text)
ip_data = json.loads(r_url_with_text)

for keys in ip_data.keys():
	print("{keydata} ==> {key_value_data}".format(keydata = keys, key_value_data = ip_data[keys]))