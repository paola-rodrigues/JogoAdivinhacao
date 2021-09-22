print("**********************************")
print('Bem-vindo ao Jogo de Adivinhação!')
print("**********************************")

print ("estou pensando no número entre 0 e 20")

numero_secreto     = 9
total_de_tentativas = 4
rodada              = 1

while(rodada <= total_de_tentativas):
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
    rodada = rodada + 1    
    
print("Fim do Jogo")    
    


 

    
    
