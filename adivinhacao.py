print("**********************************")
print('Bem-vindo ao Jogo de Adivinhação!')
print("**********************************")

print ("estou pensando no número entre 0 e 20")
print()
numero_secreto = 9

chute = input("Digite o seu numero: ")

print("Você digitou ", chute)
numero = int(chute)

if(numero_secreto == numero):
    print("Você acertou")
else:
    if(numero > numero_secreto):
        print("Você errou! O seu chute foi maior do que o número secreto.")
    elif(numero < numero_secreto):
        print("Você errou! O seu chute foi menor do que o número secreto.")
    
print("Fim do Jogo")    
    


 

    
    
