import json
from pprint import pprint

data = {
    'name' : 'Sumeet',
    'shares' : 2000,
    'value' : 5000
}

json_str = json.dumps(data)

print(json_str)

data2 = json.loads(json_str)

print(data2)
