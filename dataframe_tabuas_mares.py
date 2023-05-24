#instale as bibliotecas

# pip install requests
# pip install beautifulsoup4
# pip install pandas
# pip install lxml


import requests
from bs4 import BeautifulSoup
import pandas as pd

# define a URL do site
url = 'https://www.tide-forecast.com/locations/Belem-Para-Brazil/tides/latest'

# faz a requisição HTTP para a URL
response = requests.get(url)

# cria um objeto BeautifulSoup com o conteúdo da página
soup = BeautifulSoup(response.content, 'html.parser')

# encontra a tabela desejada e extrai os dados para um dataframe
table = soup.find('div', {'class': 'tide-header-today tide-header__card'})
df = pd.read_html(str(table))[0]

# renomeia as colunas do dataframe
df = df.rename(columns={'Tide': 'Tide', 'Time & Date': 'Time (-03) & Date', 'Height': 'Height'})

# imprime o resultado
print(df.to_string(index=False))