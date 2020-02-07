"""
note: to be able to use this file, make sure you have downloaded the following
* pip install requests
"""


import requests
import json #to convert dectionary to string

key = "e590cbc1847a0926a6bd3c93b70dc0e9"

url = "http://api.weatherstack.com/current"
n='y'

while True:
        if n == 'n':
                break

        city = input("enter City or ZIP Code or Coordinates (Lat,Lon) or IP Address	: ").strip()
        params = {
                "access_key": key,
                "query": city
        }
        res = requests.get(url, params=params)
        res = json.loads(res.text)
        print('Current tempreture in ',city,'is', res['current']['temperature'],'℃')
        n=input('Do You Want to Continue? if yes press any key if no press "n"')


