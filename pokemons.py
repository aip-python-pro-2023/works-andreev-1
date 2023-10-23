import requests

data = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
if data.ok:
    print('Success!')
    ditto = data.json()
    print(ditto["name"])
    print(ditto["weight"])
else:
    print('Failed to fetch')
