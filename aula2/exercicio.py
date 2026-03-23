'''
Crie um app que solicite duas notas de usuário,
após calcule a media das notas. Se a media for maior ou igual a 6
mostre uma mensagem que o aluno está aprovado. Se a média 
for menor que 6, peça para o aluno digitar a nota do exame final 
((media + exame final) / 2) se a media final for maior que 6 mostre 
a mensagem aprovado, senão que ele foi reprovado.
'''
nota1 = float(input("Digite sua nota 1: "))
nota2 = float(input("Digite sua nota 2: "))
media = (nota1 + nota2) / 2
if media >= 6:
    print("Aluno aprovado")
else:
    exame_final = float(input("Digite a nota do exame final:"))
    nova_media = (media + exame_final) / 2

    if nova_media >= 6:
        print ("aluno aprovado")
    else:
        print("reprovado")

'''
media = (nota1 + nota2) / 2
if media >= 6:
    print("Aluno aprovado")
else:
    exame_final = float(input("Digite a nota do exame final"))
    nova_media = (media + exame_final) / 2

    if nova_media >= 6:
        print ("aluno aprovado")
    else:
        print("reprovado")

           print("Aprovado")
elif media <6 :
    exf = float(input("Digite sua nota do exame final: "))
    mediaexf = ((media + exf) /2)
if mediaexf > 6:
    print("Voce foi aprovado")
else :
    print("Voce foi reprovado")
'''