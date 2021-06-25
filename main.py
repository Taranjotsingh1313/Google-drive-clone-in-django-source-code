import requests

r = requests.post("https://www.instagram.com/login/ajax")
print(r.json)