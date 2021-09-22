print("**********************************")
print('Bem-vindo ao Jogo de Adivinhação!')
print("**********************************")

print ("estou pensando no número entre 0 e 20")

numero_secreto     = 9
total_de_tentativas = 4
rodada              = 1

for rodada in range (1, total_de_tentativas + 1):
    print ("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = input("Digite o seu numero: ")
   

    print("Você digitou ", chute)
    numero = int(chute)

    acertou = numero == numero_secreto
    maior   = numero > numero_secreto
    menor   = numero < numero_secreto

    if(acertou):
        print("Você acertou")
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")
  
    
print("Fim do Jogo")    
    


 

    
    
