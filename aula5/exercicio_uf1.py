'''
crie um script que usa a função quadrado
criada no arquivo exercicio_f1.py. Esse 
script deve pedir para o usuário digitar um 
número, depois deve calcular o quadrado usando
a função e depois imprimir o resultado. 
'''
import exercicio_f1 as funcao

#usando funções
funcao.imprimir("Digite um numero")
n1 = funcao.ler()

resposta = funcao.quadrado(n1)
funcao.imprimir(f'O resultado é {resposta}')