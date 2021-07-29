# Calcular a  média de uma aluno.

def resultado_final():
    aluno = input("Digite seu nome!")
    print("Seu nome é: " + aluno)
    nota_1 = int(input("digite sua primeira nota: "))
    nota_2 = int(input("digite sua segunda nota: "))
    nota_3 = int(input("digite sua terceira nota: "))
    nota_4 = int(input("digite sua quarta nota: "))
    media = (nota_1 + nota_2 + nota_3 + nota_4)/4
    
    print("A media do aluno(a) " + aluno + " foi igual a " , media )
    if media >= 7 :
        print("Parabéns " + aluno + " você foi aprovado.")
    else:
        print("Lamentamos " + aluno + " infelizmente você esta de recuperação.")

resultado_final()
