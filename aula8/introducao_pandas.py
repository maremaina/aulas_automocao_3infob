import pandas as pd

#ler  a planilha do Exel utilizando pandas
planilha = pd.read_excel("aula8\\alunoss.xlsx")

#imprime a variavel planilha
print(planilha)

#imprimir os dados do aluno Pablo
print(planilha.loc[5, ["Nome", "Idade"]])

#atualizar dados
planilha.loc[5, "Nome]"] = "Pablo Sandi"
planilha.loc[5,["Nome","Idade"]] = ["Pablo Sandi Souza", 20]

#inserir um novo registro
planilha.loc[len(planilha), ["Nome", "Idade"]] = ["Ivan",40]

#imprime novamente a planilha
print(planilha)