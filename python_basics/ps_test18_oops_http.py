import requests # third party module - read it in pypi - request
from pprint import pprint as pp

url = "https://api.github.com/users/ravijaya/repos"
result = requests.get(url,)
print(result.status_code)
pp(result.json())