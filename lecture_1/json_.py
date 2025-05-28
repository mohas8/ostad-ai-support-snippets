import json

json_str = {"message": "Hello, Ostad!", "number": 42, "boolean": True, "array": [1, 2, 3], "object": {"key": "value"}}
# json_str = json.dumps(json_str, indent=4)
# print(json_str)

# json_str['new'] = "New Value"

data = json.dumps(json_str)
print(data)

#save to output.json

with open('output.json', 'w') as f:
    json.dump(json_str, f, indent=10)