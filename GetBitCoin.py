import requests
from datetime import datetime
import pandas as pd

#URL
url = "https://api.coinbase.com/v2/prices/spot"

# Requisição GET para a API
response = requests.get(url)
data = response.json()

#Entrair dados
preco = float(data['data']['amount'])
ativo = data['data']['base']
moeda = data['data']['currency']
horario_de_coleta = datetime.now()

df = dataframe = pd.DataFrame([{
    'ativo': ativo,
    'preco': preco,
    'moeda': moeda,
    'horario_de_coleta': horario_de_coleta
}])