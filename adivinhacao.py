import random


print("**********************************")
print('Bem-vindo ao Jogo de Adivinhação!')
print("**********************************")

print ("Estou pensando no número entre 0 e 20")

numero_secreto     = random.randrange(1,21)
total_de_tentativas = 4
rodada              = 1

print(numero_secreto)

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
        print("Você acertou")
        break;
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")
  
    
print("Fim do Jogo")    
    


 

    
    
