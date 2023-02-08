# API

import requests

class Pokemon():
    def __init__(self, name):
        self.name = name
        self.types = None
        self.weight = None
        self.abilities = None
        self.sprite = None
        self.poke_api_call()

    def poke_api_call(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.name}/"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self.name = data["name"]
            self.weight = data["weight"]
            types = data["types"]
            self.types = list(map(lambda x: x["type"]["name"], types))
            abilities = data["abilities"]
            self.abilities = list(map(lambda x: x["ability"]["name"], abilities))
            self.sprite = data["sprites"]["front_default"]
        else:
            print(f"Error, Status Code {response.status_code}")

pikachu = Pokemon("pikachu")
pikachu.sprite
