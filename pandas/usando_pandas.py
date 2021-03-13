import pandas as pd

data = {
        'Alunos': ['Pedro', 'Artur', 'joao', 'maria', 'bruna', 'marco', 'flavio'],
        'Idade':[19, 16, 27, 38, 18, 25, 49],
        'Notas': [10, 9, 8, 7, 6, 9, 7]
        }

df = pd.DataFrame(data, columns=['Alunos', 'Idade', 'Notas'])

print(df.describe())
print(df)

# df = df.drop([2, 3])
# print(df)
# df = df.drop('Idade' , axis=1)
# print(df)
# print(df.count())
# print(df.columns)
# print(df.shape)

# print(df['Notas'].max()) #maior
# print(df['Notas'].min()) #menor

# print(df['Notas'].mean()) #media
# print(df['Idade'].mean())

# print(df['Notas'].sum()) #soma

# df_1 = df['Idade'].add(10) #adciona
# print(df_1)

# df_2 = df['Notas'].sub(2) #subtrai
# print(df_2)

# print(df.head()) #mostra 5 primeiros
# print(df.tail()) #mostra 5 ultimos

# print(df.loc[df['Notas'] >= 8]) #mostra notas > 8
# print(df.loc[df['Idade'] >= 30]) #mostra idade > 30




