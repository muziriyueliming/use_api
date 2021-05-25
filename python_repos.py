import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=starts'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
respons_dict = r.json()

print(respons_dict.keys())