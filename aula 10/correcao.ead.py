'''
1) Considere que a tabela abaixo representa uma planilha do Excel chamada
estudantes.xlsx. Crie o código para importar a bibliote pandas e para ler a planilha
do Excel para um DataFrame chamado tabela.
'''
import pandas as pd 
alunos = pd.read_excel("aula10\\dados.xlsx", sheet_name = "alunos")
'''
2) Crie o código para exibir os 5 primeiros registros do DataFrame.
'''
print(alunos.head(5))
'''
3) Crie o código para Inserir um novo aluno no DataFrame com os seguintes dados:
● RA: 0005
● Nome: Enzo Moreira
● Curso: Técnico em Jogos
● Turma: 1GMA
'''
alunos.loc[len(alunos)] = [8, "Enzo Moreira", "Técnico em jogos" ,"1GMA"]
'''
4) Crie o código para atualizar os dados do estudante Enzo Moreira para:
● Curso: Técnico em Informática
● Turma: 3TE
'''
alunos.loc[7] = [8, "Enzo Moreira", "Técnico em Informática" ,"1TE"]
print(alunos)
'''
5) Crie o código para excluir o estudante que está na linha de índice 1 do
DataFrame.
'''
alunos.drop(0, inplace = True)
print(alunos )

'EXERCICIOS AULA 10'

'''
1. Leitura de Dados

Carregue o arquivo Excel chamado notas_estudantes.xlsx da seguinte forma:
Armazene os dados da aba "Notas" em um DataFrame chamado df_notas.
Armazene os dados da aba "Atividades" em um DataFrame chamado df_atividades.
'''
import pandas as pd

df_notas = pd.read_excel("notas_estudantes.xlsx", sheet_name="Notas")
df_atividades = pd.read_excel("notas_estudantes.xlsx", sheet_name="Atividades")

'''
2. Inserção de Registro

Adicione um novo registro ao DataFrame df_notas com os seguintes dados:
Nome: Lucas Silva
Atividade: Prova Final
Nota: 8.5
'''
df_notas.loc[len(df_notas)] = ["Lucas Silva", "Prova Final", 8.5]

'''
3. Atualização de Dados

No DataFrame df_notas, atualize para 9.0 a nota da atividade
'Trabalho 1' da estudante 'Ana Souza'.
'''
df_notas.loc[
    (df_notas["Nome"] == "Ana Souza") &
    (df_notas["Atividade"] == "Trabalho 1"),
    "Nota"
] = 9.0

print(df_notas)

'''
4. Exclusão de Registro

Exclua de df_notas o registro do estudante
'Pedro Santos' referente à atividade 'Prova 1'.
'''
df_notas.drop(
    df_notas[
        (df_notas["Nome"] == "Pedro Santos") &
        (df_notas["Atividade"] == "Prova 1")
    ].index,
    inplace=True
)

print(df_notas)

'''
5. Filtragem Simples

Selecione todos os registros de df_notas
em que a nota seja maior que 7.0.
'''
print(df_notas[df_notas["Nota"] > 7.0])

'''
6. Agrupamento e Agregação

Agrupe os dados de df_notas pelo nome dos estudantes
e calcule a média das notas de cada um deles.
'''
media = df_notas.groupby("Nome")["Nota"].mean()
print(media)

'''
7. Projeção de Colunas

Selecione e exiba apenas as colunas
'Nome' e 'Nota' do DataFrame df_notas.
'''
print(df_notas[["Nome", "Nota"]])

'''
8. Filtragem por Texto

Selecione todos os registros do DataFrame df_notas
em que a atividade seja exatamente 'Prova Final'.
'''
print(df_notas[df_notas["Atividade"] == "Prova Final"])

'''
9. Filtragem Composta e Projeção

Selecione apenas as colunas 'Nome' e 'Atividade'
dos estudantes que obtiveram nota maior que 7.0.
'''
print(
    df_notas[df_notas["Nota"] > 7.0][["Nome", "Atividade"]]
)

'''
10. Ordenação

Ordene o DataFrame df_notas pelo nome dos estudantes
em ordem alfabética (A-Z).
'''
df_notas_ordenado = df_notas.sort_values("Nome")
print(df_notas_ordenado)

'''
11. Junção de DataFrames (Merge)

Combine os dados dos dois DataFrames
(df_notas e df_atividades) utilizando a atividade
como chave de ligação.

O resultado deve exibir, para cada linha de nota,
o valor total da atividade e o assunto abordado nela.
'''
df_completo = pd.merge(df_notas, df_atividades, on="Atividade")
print(df_completo)

'''
12. Exportação de Dados

Salve o DataFrame que foi ordenado na Questão 10
em um novo arquivo Excel chamado
notas_estudantes_ordenado.xlsx,
sem incluir o índice no arquivo final.
'''
df_notas_ordenado.to_excel("notas_estudantes_ordenado.xlsx", index=False)

'''
6) Exportar o DataFrame atualizado para uma nova planilha do Excel.
'''
alunos.to_excel("nova_planilha.xlsx")