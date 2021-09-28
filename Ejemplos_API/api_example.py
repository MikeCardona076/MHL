import requests

url = "http://172.16.2.83:8000/apis-mhl/Estudios%20y%20Perfiles%20de%20Laboratorio/"

print(requests.get(url).json())