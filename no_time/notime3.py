import grequests
import requests
import time
from datetime import datetime


base_url = "http://54.76.245.171/"
url_login = base_url + "login"

# Get timestamp two second from now, in the GMT zone
moment = int(str(time.time()).split('.')[0]) - 3600 + 2

# Convert timestamp to string (Wed, 11 Mar 2020 13:39:28 GMT)
moment_str = datetime.fromtimestamp(
    moment).strftime("%a, %d %b %Y %H:%M:%S GMT")

# Craft header
header = {
    'Date': moment_str,
}


pin = "198519891990"
data = {"pin": pin}

response = requests.post(url_login, json=data)
print(response.headers)
print(response.text)
