import pandas as pd

#1. Leitura de dados
df_notas = pd.read_excel("aula11\\notas_estudantes.xlsx", sheet_name="Notas")
df_atividades = pd.read_excel("aula11\\notas_estudantes.xlsx", sheet_name="Atividades")

#Imprimir dataframe
print(df_notas)
print(df_atividades)

#2. Inserção de Registro
df_notas.loc[len(df_notas)] = ["Lucas Silva", "Prova Final", 8.5]
#Imprimir dataframe
print(df_notas)

#3. Atualização de Dados
df_notas.loc[(df_notas['Nome'] == "Ana Souza") & (df_notas['Atividade'] == "Trabalho 1"), "Nota"] = 9
print(df_notas)

#4. Exclusão de Registro
df_notas.drop(df_notas.loc[(df_notas['Nome'] == "Pedro Santos") & (df_notas['Atividade'] == "Prova 1"), "Nota"].index, inplace=True)
print(df_notas)

#5. Filtragem Simples
resposta = df_notas.loc[df_notas['Nota'] > 7]
print(resposta)
