import requests
from tomlkit import key
from dotenv import load_dotenv
import os

# response = requests.get('https://oim.108122.xyz/words/random')
# print(response.json())   # a random word!

# response = requests.get('https://oim.108122.xyz/mass')
# data = response.json()

# print(data['name'])       # 'Massachusetts'
# print(data['governor'])   # 'Maura Healey'

# for town in data['data'][:5]:
#     print(f"{town['name']}: pop {town['population']:,}")

# # GET: read/fetch data
# requests.get('https://oim.108122.xyz/words/random')

# # POST: send/submit data
# requests.post('https://oim.108122.xyz/echo',
#               json={'name': 'Alice', 'course': 'OIM3640'})

# import requests

# response = requests.get(
#     'https://oim.108122.xyz/words/random',
#     headers={'X-Token': "chloechloe"},  # your first name x2
# )
# print(response.json())

# import requests



# # POST: send a message (1-140 characters)
# requests.post('https://oim.108122.xyz/message',
#                 json={'message': 'Hello from chloe!'},
#                 headers={'X-Token': 'chloechloe'})

# # GET: read all messages
# data = requests.get('https://oim.108122.xyz/messages').json()
# for msg in data:
#     print(msg)


response = requests.delete(
     'https://oim.108122.xyz/message',
     headers={'X-Token': 'chloechloe'}
 )
print(response.status_code)
print(response.json())

load_dotenv()  # Load environment variables from .env file
API_KEY = os.getenv('OPENWEATHER_KEY')  # Don't hardcode this!
print(API_KEY)
url = (f'https://api.openweathermap.org/data/2.5/weather'
       f'?q=Boston&appid={API_KEY}&units=imperial')
print(url)
data = requests.get(url).json()
print(f"Boston: {data['main']['temp']}°F")
#How do we protect the key?