'''
Crie um script que solicita o usuário e a senha
do estudante. Enquanto o estudante não digitar o usuário
e a senha corretamente o programa deve continuar solicitando 
as credenciais. Quando o usuário digitá-lascorretamente o 
programa deve imprimir a mensagem de bem vindo e terminar.
O usuário ea senha deve ser fixo (padrão)
usuáro = admim
senha = admin123
'''

while True:
    usuario = input("Digite seu login")
    senha = input("Digite sua senha")

    if(usuario =="admin" or senha=="admin123"):
        print ("Bem vindo ao sistema")
        break
    else:
        print("Usuário ou sena inválidos")