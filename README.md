# Scraping de Dados de Marés

Este é um programa Python que realiza o scraping de dados de marés de um site específico e exibe os dados em forma de tabela.

# Funcionalidades

- Requisição HTTP: O programa faz uma requisição HTTP para uma URL específica.
- Parsing HTML: Utilizando a biblioteca BeautifulSoup, o programa extrai o conteúdo da página e cria um objeto BeautifulSoup.
- Extração de dados: O programa encontra a tabela desejada no objeto BeautifulSoup e extrai os dados para um dataframe utilizando a biblioteca pandas.
- Renomeação de colunas: As colunas do dataframe são renomeadas.
- Exibição de resultados: O programa exibe os dados de marés em forma de tabela.

# Configuração
Antes de executar o programa, é necessário instalar as seguintes bibliotecas:

- requests
- BeautifulSoup
- pandas

Você pode instalá-las usando o seguinte comando:

- pip install requests
- pip install beautifulsoup4
- pip install pandas
- pip install lxml
