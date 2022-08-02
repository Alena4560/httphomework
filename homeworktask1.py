import requests

def get_name(json_data):
    return json_data["name"]

def get_intelligence(json_data):
    return json_data["powerstats"]["intelligence"]

def get_json_data(superhero_id):
    base_url = "https://akabab.github.io/superhero-api/api/"
    url = base_url + "/id/" + str(superhero_id) + ".json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

superhero_id = 1
found = 0
intelligence = dict()

while found < 3:
    json_data = get_json_data(superhero_id)
    if json_data == None: 
        superhero_id += 1
        continue
    name = get_name(json_data)
    if name == "Hulk" or name == "Captain America" or name == "Thanos":
        found += 1
        intelligence[name] = get_intelligence(json_data)
        print(name, " -> ", superhero_id)
    superhero_id += 1 

print(intelligence)
max_intelligence = max(intelligence.values())
for name in intelligence:
    if intelligence[name] == max_intelligence:
        print("Самый умный супергерой:", name)

