import json

with open('config.json') as config_file:
    data = json.load(config_file)

width = data['width']
height = data['height']
print(width)
print(height)
