import math
print('Você está usando Calculadora!')
print('*números inteiros apenas*')
print(' ')
opcao1 = input('Escolha seu primeiro valor')
print(' ')
print('1 para adição, 2 para subtração, 3 para divisão, 4 para multiplicação')
print('5 para potenciação')
print('')
resposta = input('Que conta você quer fazer agora?')
print('')
try:
    int(resposta)
except:
    try:
        str(resposta)
    finally:
        print('Por enquanto só temos essas as 5 operações')
if resposta > '5':
    print('Por enquanto só temos essas 5 operações')
    quit()
opcao2 = input('Agora escolha seu segundo valor')
print('')

opcao1 = int(opcao1)
opcao2 = int(opcao2)
if resposta == '1':
    calculo = opcao1 + opcao2
    print(calculo)
elif resposta == '2':
    calculo = opcao1-opcao2
    print(calculo)
elif resposta == '3':
    calculo = opcao1/opcao2
    calculo = int(calculo)
    print(calculo)
elif resposta == '4':
    calculo = opcao1*opcao2
    print(calculo)
elif resposta == '5':
    calculo = math.pow(opcao1, opcao2)
    print(calculo)
