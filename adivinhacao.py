import random

def jogar():
  numero_secreto = numero_secreto = random.randrange(1, 101)
  numero_tentativas = 0
  pontos = 100

  print(" ")
  print("*********************************")
  print("Bem vindo ao jogo da adivinhação!")
  print("*********************************")
  print(" ")
  print("Qual nível de dificuldade?")
  print("(1) Fácil (2) Médio (3) Difícil")
  print(" ")
  nivel = int(input("Defina a dificuldade: "))

  if (nivel == 1):
    numero_tentativas = 20
  elif (nivel == 2):
    numero_tentativas = 10
  elif (nivel == 3):
    numero_tentativas = 5
  else:
    print("O número digitado não é valido, a dificuldade foi selecionada como médio por padrão")
    numero_tentativas = 10

  for rodada in range(1, numero_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, numero_tentativas))
    
    chute_str = input("Digite um numero entre 1 e 100: ")
    print("Você digitou", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100): 
      print("Voce deve digitar um número entre 1 e 100!")
      continue

    acertou = chute == numero_secreto
    menor = chute < numero_secreto
    maior = chute > numero_secreto
    
    if(acertou): 
      print("Voce acertou e fez {} pontos!!"  .format(pontos))
      break
    else:
      if(maior):
        print("O numero que voce digitou é maior que o número secreto")

      elif(menor):
        print("O numero que voce digitou é menor que o número secreto")
        
      pontos_perdidos = abs(chute - numero_secreto)
      pontos = pontos - pontos_perdidos
      
  print("Fim do jogo!!")

if(__name__ == "__main__"):
  jogar()