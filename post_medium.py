import secrets
import requests
import re
from functools import reduce
from operator import add

integration_token = secrets.INTEGRATION_TOKEN

file = input('file: ')
publish_status = input('publishStatus: ') or 'draft'

user_id_res = requests.get('https://api.medium.com/v1/me', headers={ 'Authorization': f'Bearer {integration_token}' })
user_id = user_id_res.json()['data']['id']

post_url = f'https://api.medium.com/v1/users/{user_id}/posts'

headers = {
  'Authorization': f'Bearer {integration_token}',
  'Content-Type': 'application/json'
}

with open(file, 'r') as f:
  origin = f.read()

  title = origin.splitlines()[0]
  tags = re.findall(r'#([^\s]+)', origin.splitlines()[2])
  content = reduce(add, map(lambda m: m + "\n", origin.split('\n')[3:]))

  json = {
    "title": title,
    "contentFormat": 'markdown',
    "content": content,
    "tags": tags,
    "publishStatus": publish_status
  }

  requests.post(post_url, headers=headers, json=json)

print(f'{file} was posted to Medium!')
