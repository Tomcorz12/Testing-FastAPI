import requests

def getCategories():
    r = requests.get('https://api.escuelajs.co/api/v1/products')
    
    #Converitmos el string en un archivo Json
    categories = r.json()
    # Vamos a recorrer el Json para poder obtener alguna información
    for category in categories:
        print(category['images'])