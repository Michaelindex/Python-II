from os import system, name
import random

opcao = 's'
while opcao.upper()=='S':
    system('cls') if(name == 'nt') else system('clear')

    computador = random.randint(0,2)
    jogador = int(input('''Escolha uma opção para se jogar:
    [1] Pedra
    [2]Papel
    [3] Tesoura
    Digite sua escolha: '''))-1
    pecas = ("Pedra", "Papel", "Tesoura")

    tabela = (
        ('')
    )