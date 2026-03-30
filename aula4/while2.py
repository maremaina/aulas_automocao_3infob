#While 

continuar = True 

while continuar:
    print("Digite o nome do aluno")
    aluno = input()

    resp = int(input("Deseja continuar: \n0 para não \n1 para sim"))
    if resp == 0:
        continuar = False
