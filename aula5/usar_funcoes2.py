from aula4.funcao import imprimir 
from aula4.funcao import ler, somar

#usando funções
imprimir("Digite o numero1")
n1 = ler()

imprimir('Digite o número 2')
n2  = ler()

resposta = somar(n1, n2)
imprimir(f'O resultado é {resposta}')