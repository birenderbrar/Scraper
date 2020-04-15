import requests 

res = requests.get('https://github.com/birenderbrar/Scper')

print(res.raise_for_status())
