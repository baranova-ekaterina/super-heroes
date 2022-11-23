import requests

heroes = ['Hulk', 'Captain America', 'Thanos']

url = 'https://akabab.github.io/superhero-api/api/all.json'
res = requests.get(url).json()
filtered_heroes = filter(lambda hero:hero['name'] in heroes, res)

def get_hero (filtered_heroes):
    dict_names = {}
    for hero in filtered_heroes:
        dict_names[hero['name']] = hero['powerstats']['intelligence']
    return dict_names

#print(list(filtered_heroes))
heroes = get_hero(filtered_heroes)
print(max(heroes, key=heroes.get))

print(res[0])
print()
#print(res[10])

print(len(res))
#n = res.get('name', 'intelligence')
#print(n)
#print(type(res))


#def get_hero_dict(self):
    #url = 'https://akabab.github.io/superhero-api/api'
    #res = requests.get(url)
    #print(res.json())

#get_hero_dict(self)


