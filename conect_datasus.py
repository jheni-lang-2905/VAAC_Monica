'''

OBJETIVO: Realizar o tratamento de dados, utilizando métodos de apiRestFull e normalização de arquivos .csv

TAREFAS
 - extrair arquivos csv do portal datasus(dataframes)
    -> https://opendatasus.saude.gov.br/dataset?tags=Condi%C3%A7%C3%B5es (ARQUIVO)
    -> https://imunizacao-es.saude.gov.br/_search (API)
 - Normalização de dados para facilitar o manuseio desses dados
 - Salvamento em banco de dados
    -> Criação de modelagem de banco de dados
    -> criação de infraestrutura do banco
    -> hospedagem de infraestrutura
    -> inserção de dados normalizado
 - Gráficos e métricas a serem criadas(IDEIAS)
    -> Quantidade de Pessoas vacinadas em São Paulo em 2022
    -> Pessoas vacinadas por faixa étaria
    -> Ranking das vacinas mais distribuidas entre a amostragem(SP) considerando 1dose, 2dose, reforço etc(ASTRAZENICA, CORONAVAC ...)
    -> continuar ideias
'''


import json
import requests

from pandas.io.json import json_normalize


#API de comunicação com datasus
def datasus_communication_request():
    try:
        url = "https://imunizacao-es.saude.gov.br/_search"
        payload = "{\r\n    \"size\": 10\r\n}"
        headers = {
            'Authorization': 'Basic aW11bml6YWNhb19wdWJsaWM6cWx0bzV0JjdyX0ArI1Rsc3RpZ2k=',
            'Content-Type': 'application/json'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        transform_dataset_analyze(response.text)
    except Exception as e:
        print(e)

#função de criação de dataset
def transform_dataset_analyze(response):
    resul = json.loads(response)
    df = json_normalize(resul["hits"]["hits"])
    print(df)


#método main para chamar os demais métodos
if __name__ == '__main__':
    datasus_communication_request()