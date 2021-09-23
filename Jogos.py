import jogoForca
import adivinhacao

def escolhe_jogo():
      print("**********************************")
      print("********Escolha o seu jogo*******!")
      print("**********************************")


      print("(1) Forca (2) Adivinhação")

      jogo = int(input("Qual jogo?"))

      if(jogo == 1 ):
            print("jogando Forca")
            jogoForca.jogar()
      elif(jogo == 2 ):
            print("jogando Adivinhação")
            adivinhacao.jogar()
      
if(__name__ == "__main__"):
      escolhe_jogo()



      
 
      
