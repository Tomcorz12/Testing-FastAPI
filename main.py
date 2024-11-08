from fastapi import FastAPI
import request

app = FastAPI() # Creamos una instancia para la aplicación

#Creamos un decorador para poder ver en la web la información
@app.get('/')

def getList():
    return "Página Principal"

@app.get('/images')

def getList():
    return "Acá van las imágenes"