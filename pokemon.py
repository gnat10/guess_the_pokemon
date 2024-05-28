import requests
import random
import os


class Pokemon:

    def random_pokemon(self: str):
        with open(f'{self}', 'r') as f:
            pokemon = f.read().splitlines()
            chosen_pokemon = random.choice(pokemon)
            return chosen_pokemon

    def save_pokemon_image(self: str):
        image_url = f'https://projectpokemon.org/images/normal-sprite/{self}.gif'
        #image_url = f'https://img.pokemondb.net/sprites/x-y/normal/{self}.png'
        #image_url = f'https://img.pokemondb.net/artwork/large/{self}.jpg'
        img_data = requests.get(image_url).content
        with open(f'./data/pokemon_image/{self}.gif', 'wb') as handler:
            handler.write(img_data)
        return img_data

    def delete_pokemon_image(self: str):
        os.remove(self)
        return

