import requests
import tabulate
import telebot
import json

with open('data.json') as file:
    data = json.load(file)

print(data['marks'])

data['age'] = 87

with open('result.json', 'w') as result:
    json.dump(data, result, indent=2)
