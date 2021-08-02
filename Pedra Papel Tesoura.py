import random

print('')
print('Você está jogando Pedra, Papel ou Tesoura!')
print('')

opcoes = ['pedra', 'papel', 'tesoura']
pontos_jogador = 0
pontos_robo = 0
while pontos_jogador < 3:
    player_choice = str(input('Qual será a sua jogada?')).lower()
    robo_choice = random.choice(opcoes)
    if pontos_robo == 3:
        print('Putz, o robô chegou primeiro a 3 pontos, perdeu.')
        print("     _______________         ")
        print("    /               \       ")
        print("   /                 \      ")
        print("/\/                   \/\  ")
        print("\ |   XXXX     XXXX   | /   ")
        print(" \|   XXXX     XXXX   |/     ")
        print("  |   XXX       XXX   |      ")
        print("  |                   |      ")
        print("  \__      XXX      __/     ")
        print("    |\     XXX     /|       ")
        print("    | |           | |        ")
        print("    | I I I I I I I |        ")
        print("    |  I I I I I I  |        ")
        print("    \_             _/       ")
        print("      \_         _/         ")
        print("        \_______/           ")
        exit()
    if player_choice == robo_choice:
        print('Empate! Ninguém ganha ponto.')
    if player_choice != robo_choice:
        if player_choice == 'papel' and robo_choice == 'pedra':
            print('Boa! Você jogou {} e o robô "escolheu" {}'. format(player_choice,robo_choice))
            print('Papel ganha de pedra')
            pontos_jogador += 1
            print('Você está com {} pontos e o robô está com {} pontos'.format(pontos_jogador, pontos_robo))
        if player_choice == 'papel' and robo_choice == 'tesoura':
            print('Putz, você jogou {} e o robô "escolheu" {}'. format(player_choice,robo_choice))
            print('Tesoura ganha de papel')
            pontos_robo += 1
            print('Você está com {} pontos e o robô está com {} pontos'.format(pontos_jogador, pontos_robo))
        if player_choice == 'pedra' and robo_choice == 'papel':
            print('Putz, você jogou {} e o robô "escolheu" {}'. format(player_choice,robo_choice))
            print('Papel ganha de pedra')
            pontos_robo += 1
            print('Você está com {} pontos e o robô está com {} pontos'.format(pontos_jogador, pontos_robo))
        if player_choice == 'pedra' and robo_choice == 'tesoura':
            print('Boa! Você jogou {} e o robô "escolheu" {}'. format(player_choice,robo_choice))
            print('Pedra ganha de tesoura')
            pontos_jogador += 1
            print('Você está com {} pontos e o robô está com {} pontos'.format(pontos_jogador, pontos_robo))
        if player_choice == 'tesoura' and robo_choice == 'pedra':
            print('Putz, você jogou {} e o robô "escolheu" {}'. format(player_choice,robo_choice))
            print('Pedra ganha de tesoura')
            pontos_robo += 1
            print('Você está com {} pontos e o robô está com {} pontos'.format(pontos_jogador, pontos_robo))
        if player_choice == 'tesoura' and robo_choice == 'papel':
            print('Boa! Você jogou {} e o robô "escolheu" {}'. format(player_choice,robo_choice))
            print('Tesoura ganha de papel')
            pontos_jogador += 1
            print('Você está com {} pontos e o robô está com {} pontos'.format(pontos_jogador, pontos_robo))
if pontos_jogador == 3:
        print('Parabéns, você ganhou da máquina')
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
        exit()