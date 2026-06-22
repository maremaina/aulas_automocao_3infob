                #Importar a biblioteca do pandas
import pandas as pd

                #Carregar uma planilha do Excel
#df = dataframe 
df = pd.read_excel('aula12/planilha.xlsx')
print(df.head())

#loc= localizar 
print(df.loc[0])#imprime a primeira linha 
print(df.loc[0,"Nome"]) #imprime a coluna Nome da primeira linha
print(df.loc[0 : 3]) #0 = linha inicial 3 = linha final
print(df.loc[0 : 3, "Nome"]) #somente os nomes das 4 primeiras pessoas
print(df.loc[0 : 3, ["Nome","Idade"]]) #somente os nomes e a idade das 4 primeiras pessoas
print(df.loc[ : , "Nome"]) # : = entende que é para pegar todas as linhas e exibe só os nomes 

df2 = df.loc[3:6, ["Nome", "Sexo"]]
print(df2) #vai pegar das linhas 3 a 6 e exibir somente o nome e o sexo
print (df2.loc[[True, False,False,True],["Nome", "Sexo"]]) # exibe em uma ordem que eu queira mas somente do df2, o df nao vai imprimir pois ele le como as 30 linhas da planilha

                    #Atualizar dados na planilha
#Inserir novos dados da planilha
#df.loc[100] = Nome, Sexo, Idade, Curso, Disciplina, Nota
df.loc[len(df)] = ["Isis","Feminino",18,"Informática", "Automoção T",10] #coloca um novo dado na planilha #len(df) = localiza o próximo valor da lista que no caso é 30
print(df) #imprime a planilha toda

#Atualizar dados na planilha
df.loc[30, ["Curso", "Disciplina"]] = ["Artes","Teatro"]
print(df) # muda o curso e a disciplina da pessoa que está na linha 30 

#Filtrar dados
condicao = df["Idade"] == 20
print(df.loc[condicao])
#imprime só os que tem 20 anos 

#condicao2 = df["Sexo"] == "Feminino"
#print(df.loc[condicao2])
#imprime só o sexo feminino 

condicao2 = df["Sexo"] == "Feminino"
print(df.loc[condicao & condicao2, "Nome"])

#imprime só os nomes do sexo feminino que tem 20 anos



                    #Classificar dados
tabela_ordenada = df.sort_values("Nome", ascending = True) #coloca a tabela toda em ordem alfabética
print(tabela_ordenada)



                    #Contar dados
tabela_contagem = df.value_counts("Sexo")
print(tabela_contagem) #conta quantas pessoas tem de cada sexo 
 
tabela_contagem = df.value_counts("Curso")
print(tabela_contagem) #conta quantas pessoas tem de cada curso


#Agrupar dados
tabela_agrupada = df.groupby("Sexo")["Sexo"].count()
print(tabela_agrupada)

#Exportar dados 
df.to_excel("aula12\\nova_planilha.xlsx")