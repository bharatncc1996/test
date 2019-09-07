#scratch data from a website

import json
import requests
r = requests.get('https://www.xkcd.com/')
print(r.headers)

