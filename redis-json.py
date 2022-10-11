import re
import redis
from redis.commands.json.path import Path   


client = redis.Redis(host='192.168.183.135', port = 6379)

jane = {
     'name': "Jane", 
     'Age': 33, 
     'Location': "Chawton"
   }

print(client)

client.json().set('person:1', Path.root_path(), jane)

result = client.json().get('person:1')
client.set('key1',12)

print(result)