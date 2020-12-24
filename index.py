from bs4 import BeautifulSoup

import requests

html = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/350/bentogoncalves-rs").content

soup = BeautifulSoup(html, 'html.parser')

temperaturaMinima = soup.find(id="min-temp-1").string
temperaturaMaxima = soup.find(id="max-temp-1").string

print((temperaturaMinima, temperaturaMaxima))