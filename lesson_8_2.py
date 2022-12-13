import requests

TOKEN = "  "  # ТОКЕН !!!!!
base_host = 'https://cloud-api.yandex.net/'
uri = 'v1/disk/resuorces/upload/'
PREPARE_UPLOAD_URL = base_host + uri
params = {'path': '/test_file.txt', 'overwrite': 'true'}
headers = {'Accept': 'application/json', 'Authorization': TOKEN}

file_path = 'c:/Users/glesh/netology/super_heroes/test_file.txt'

response = requests.get(PREPARE_UPLOAD_URL, params=params, headers=headers)
print(response.text)

put_url = response.json().get('href')
print(put_url)

files = {'file': open(file_path, 'rb')}
response = requests.put(put_url, files=files, headers=headers)
print(response)

