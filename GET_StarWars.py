import pandas as pd
import requests


class Get_StarWars:
    def __init__(self, url):
        if url == 'https://swapi.dev/api/planets/':
            self.url_plan = url
        elif url == 'https://swapi.dev/api/people/':
            self.url_person = url
        elif url == 'https://swapi.dev/api/species/':
            self.url_species = url
        else:
            raise Exception('URL inválida')

    def getPlanetas(self, plan):
        cont = 0
        planetas = []
        while cont < plan:
            cont += 1
            planetas.append(str(cont))
        lista_colunas = []
        for coluna in planetas:
            JSONContent = requests.get(self.url_plan + coluna).json()
            if 'error' not in JSONContent:
                lista_colunas.append([JSONContent['name'], JSONContent['rotation_period'], JSONContent['orbital_period'],
                        JSONContent['diameter'], JSONContent['climate'], JSONContent['gravity'], JSONContent['terrain'],
                        JSONContent['surface_water'], JSONContent['population'], JSONContent['residents'],
                        JSONContent['films'], JSONContent['created'], JSONContent['edited'], JSONContent['url']])

        dataset = pd.DataFrame(lista_colunas)
        dataset.columns = ['name', 'rotation_period', 'orbital_period', 'diameter', 'climate', 'gravity', 'terrain',
                           'surface_water', 'population', 'residents', 'films', 'created', 'edited', 'url']
        return dataset

    def getPessoas(self, person):
        cont = 0
        personagens = []
        while cont < person:
            cont += 1
            personagens.append(str(cont))
        lista_colunas = []
        for coluna in personagens:
            JSONContent = requests.get(self.url_person+ coluna).json()
            if 'error' not in JSONContent:
                lista_colunas.append(
                    [JSONContent['name'], JSONContent['height'], JSONContent['mass'],
                     JSONContent['hair_color'], JSONContent['skin_color'], JSONContent['eye_color'],
                     JSONContent['birth_year'], JSONContent['gender'], JSONContent['homeworld'], JSONContent['films'],
                     JSONContent['species'], JSONContent['vehicles'], JSONContent['starships'], JSONContent['created'],
                     JSONContent['edited'], JSONContent['url']])

        dataset = pd.DataFrame(lista_colunas)
        dataset.columns = ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year',
                               'gender', 'homeworld', 'films', 'species', 'vehicles', 'starships', 'created', 'edited', 'url']
        return dataset

    def getSpecies(self, especies):
        cont = 0
        species = []
        while cont < especies:
            cont += 1
            species.append(str(cont))
        lista_colunas = []
        for coluna in species:
            JSONContent = requests.get(self.url_species + coluna).json()
            if 'error' not in JSONContent:
                lista_colunas.append([JSONContent['name'], JSONContent['classification'], JSONContent['designation'],
                                      JSONContent['average_height'], JSONContent['skin_colors'],
                                      JSONContent['hair_colors'], JSONContent['eye_colors'],
                                      JSONContent['average_lifespan'], JSONContent['homeworld'],
                                      JSONContent['language'], JSONContent['people'],
                                      JSONContent['films'], JSONContent['created'], JSONContent['edited'],
                                      JSONContent['url']])

        dataset = pd.DataFrame(lista_colunas)
        dataset.columns = ['name', 'classification','designation', 'average_height', 'skin_colors', 'hair_colors',
                           'eye_colors', 'average_lifespan', 'homeworld', 'language', 'people', 'films', 'created',
                           'edited', 'url']
        return dataset


a = Get_StarWars('https://swapi.dev/api/planets/')
b = a.getPlanetas(10)
