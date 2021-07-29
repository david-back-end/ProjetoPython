# Projeto para saber o valor de qualquer tabuada



limite = 10
multiplicador = 0
tabuada = int(input("Qual a tabuada?: "))
while multiplicador <= limite:
    resultado = tabuada * multiplicador
    print( tabuada,"x" , multiplicador,"=", resultado , "\n")
    multiplicador = multiplicador + 1 

    
