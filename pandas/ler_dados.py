import pandas as pd

# ler em excel
# dados_ex = pd.ExcelFile('nome_arquivo.xlsx)
# dados = pd.read_excel(dados_ex, 'planilha_1')
# vai criar data frame

dados = pd.read_csv('servicos.csv')

print(dados.describe())

print(dados.columns)

dados = dados.drop('CPC', axis=1)
dados = dados.drop('Subclasse', axis=1)
dados = dados.drop('Unidade medida', axis=1)

print(dados)
