# Menu de opções

print( "OP:1 = Abrir LOL - OP:2 = Fechar LOL - OP:3 = Abrir COD - OP:4 = Fechar COD - OP:5 = Sair do menu")

def opcao(menu = 0):
    menu = int(input("Escreva sua OP: "))
    if(menu == 1):
        print("Abrindo o lol...")

    if(menu == 2):
        print("Fechando o LOL...")

    if(menu == 3):
        print("Abrindo o COD....")

    if(menu == 4):
        print("Fechando o COD...")

    if(menu == 5):
        print("Saindo do menu...")

opcao()
    



  



