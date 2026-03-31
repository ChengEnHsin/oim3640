import requests

response = requests.get('https://oim.108122.xyz/words/random')
print(response.json())   # a random word!

response = requests.get('https://oim.108122.xyz/mass')
data = response.json()

print(data['name'])       # 'Massachusetts'
print(data['governor'])   # 'Maura Healey'

for town in data['data'][:5]:
    print(f"{town['name']}: pop {town['population']:,}")

# GET: read/fetch data
requests.get('https://oim.108122.xyz/words/random')

# POST: send/submit data
requests.post('https://oim.108122.xyz/echo',
              json={'name': 'Alice', 'course': 'OIM3640'})

import requests

response = requests.get(
    'https://oim.108122.xyz/words/random',
    headers={'X-Token': "chloechloe"},  # your first name x2
)
print(response.json())