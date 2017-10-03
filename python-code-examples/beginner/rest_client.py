from simple_rest_client.api import API
from pprint import pprint
import json

api = API("https://jsonplaceholder.typicode.com/", 
          {}, 
          {}, 
          3000, 
          False, 
          True)

api.add_resource(resource_name="posts")
print ("Printing list of actions supported by POSTS resource")
#data = json.load(str(actions))
pprint (api.posts.actions)
response = api.posts.list()

print ("Response URL:"+ response.url)
print ("Response Status code:" + str(response.status_code))
print ("Response Body:" + str(response.body))