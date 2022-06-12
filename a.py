import json
# import pandas as pd
import requests

# url = 'http://getbible.net/json?passage=Jn3:16'
url = "https://bible-api.com/john 3:16"
r = requests.get(url)
r_text = r.text
r_json = r.json()
# r_text.encode('utf-8')
print(r_json)
# print("The type of object is: ", type(r_json))
print(r_json["text"])
# stud_obj = json.loads(r_text)
# print(stud_obj)
# print("The type of object is: ", type(stud_obj))
# if response.status_code != 204:
#     data = json.loads(response.json)
#     print(data)
