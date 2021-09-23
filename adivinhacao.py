import random


print("**********************************")
print('Bem-vindo ao Jogo de Adivinhação!')
print("**********************************")

print ("Estou pensando no número entre 0 e 20")

numero_secreto     = random.randrange(1,21)
total_de_tentativas = 0
rodada              = 1
pontos = 100

print ("Qual nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Díficil")

nivel = int(input("Defina o nível: "))

if(nivel == 1):
    total_de_tentativas = 10
elif(nivel == 2):
    total_de_tentativas = 6
elif(nivel == 3):
    total_de_tentativas = 4  
else:
    print ("não existe esse nível, inicie novamente!")
   

for rodada in range (1, total_de_tentativas + 1):
    print ("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = input("Digite o seu numero: ")
    print("Você digitou ", chute)
    numero = int(chute)
    
    if(numero < 1 or numero > 20):
        print ("Você deve digitar um número entre 0 e 20!")

    

    acertou = numero == numero_secreto
    maior   = numero > numero_secreto
    menor   = numero < numero_secreto

    if(acertou):
        print("Você acertou e fez {} pontos!".format(pontos))
        break;
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")
        pontos_perdidos = abs (numero_secreto - numero)
        pontos = pontos - pontos_perdidos 
    
print("Fim do Jogo")    
    


 

    
    
