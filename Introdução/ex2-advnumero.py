from os import system
import random

system('cls')

print("***************************")
print(" Adivinhe o número ")
print("***************************")

numero_secreto = random.randrange(0,101)
total_tentativas = 10

for rodada in range(1, total_tentativas + 1):
    print(f"\nTentativa {rodada:02d} de {total_tentativas:02d}")

    tentativa = input(" Tente acertar o número de 1 a 100: ")
    print("Você digitou: ",tentativa)

    tentativa_int = int(tentativa)
    if(tentativa_int < 1 or tentativa_int > 100):
        print("Tentativa INVÁLIDA! Somente números de 1 a 100!")
        continue
    acerto = tentativa_int == numero_secreto
    ehmaior = tentativa_int > numero_secreto
    ehmenor = tentativa_int < numero_secreto
    if (acerto):
        print("Boa tentativa. ACERTOU!!")
        break
    else:
        print("Não foi dessa vez, você errou !")

        if(ehmaior):
            print("Sua tentativa foi MAIOR que o número secreto")
        if(ehmenor):
            print("Sua tentativa foi MENOR que o número secreto")
print(f'O número secreto sorteado foi: {numero_secreto}')
input('\nObrigado por participar!\n')