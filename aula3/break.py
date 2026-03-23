#comando break: interrompe o laço de repetição

nomes = ["Lucas", "Jesuely", "Caua", "Filipe"]
nome_iniciado_com_c = ""
for nome in nomes:
    if nome.startswitch("C"):
       nome_iniciado_com_c = nome
       break
    print (nome)

print("O primeiro np0me iniciado com C é", nome_iniciado_com_c)