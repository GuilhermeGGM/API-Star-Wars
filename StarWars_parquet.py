import pandas as pd
import requests

def get_api(plan):
    cont = 0
    planetas = []
    while cont < plan:
        cont =+ 1
        cont2 = str(cont)
        planetas.append(cont2)
    lista_colunas = []
    for coluna in planetas:
        JSONContent = requests.get('https://swapi.dev/api/planets/' + coluna).json()
        if 'error' not in JSONContent:
            lista_colunas.append([JSONContent['name'], JSONContent['rotation_period'], JSONContent['orbital_period'],
                    JSONContent['diameter'], JSONContent['climate'], JSONContent['gravity'], JSONContent['terrain'],
                    JSONContent['surface_water'], JSONContent['population'], JSONContent['residents'],
                    JSONContent['films'], JSONContent['created'], JSONContent['edited'], JSONContent['url']])

    dataset = pd.DataFrame(lista_colunas)
    dataset.columns = ['name', 'rotation_period', 'orbital_period', 'diameter', 'climate', 'gravity', 'terrain',
                       'surface_water', 'population', 'residents', 'films', 'created', 'edited', 'url']
    return dataset
df = get_api(10)

df.to_parquet('StarWars.parquet2')
