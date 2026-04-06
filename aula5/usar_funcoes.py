import aula4.funcao as funcao

#usando funções
funcao.imprimir("Digite o numero1")
n1 = funcao.ler()

funcao.imprimir('Digite o número 2')
n2  = funcao.ler()

resposta = funcao.somar(n1, n2)
funcao.imprimir(f'O resultado é {resposta}')