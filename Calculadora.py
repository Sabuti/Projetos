import math

print('')
print('Você está usando Calculadora!')
print(' ')
escolha = input('Se não quiser função quadrática digite 1, se quiser 2: ')
if escolha == '2':
    a = float(input('Qual o valor de a? '))
    b = float(input('Qual o valor de b? '))
    c = float(input('Qual o valor de c? '))
    delta = b**2 - (4*a*c)
    raiz = math.sqrt(delta)
    conta_positivo = (-b+raiz)/(2*a)
    conta_negativo = (-b-raiz)/(2*a)
    print('Delta deu {}, x positivo deu {} e x negativo deu {}'.format(delta,conta_positivo,conta_negativo))
else:
    opcao1 = float(input('Escolha seu primeiro valor: '))
    print(' ')
    print('1 para adição, 2 para subtração, 3 para divisão, 4 para multiplicação')
    print('5 para potenciação, 6 para raiz, 7 para logaritmo, 8 para fatorial')
    print('73 para bônus')
    print('')
    resposta = input('Que conta você quer fazer agora? ')
    print('')

    try:
        float(resposta)
    except:
        try:
            str(resposta)
        finally:
            print('Por enquanto só temos essas as 8 operações')
            print('Por favor, escolha um dos números acima')
            exit()
    if resposta > '8':
            print('Por enquanto só temos essas 8 operações')
            quit()
    if resposta == '6':
        calculo = math.sqrt(opcao1)
        calculo = float("{0:.2f}".format(calculo))
        print(calculo)
        exit()
    if resposta == '7':
        opcao2 = int(input('Agora escolha a base que você quer: '))
        calculo = math.log(opcao1,opcao2)
        print(calculo)
        exit()
    if resposta == '8':
        opcao1 = int(opcao1)
        resultado = math.factorial(opcao1)
        print(resultado)
        exit()
    if resposta == '73':
        identidade_de_Euler = math.e**(math.pi*1j)+1
        print('imprimindo Identidade de Euler:', identidade_de_Euler)

    opcao2 = float(input('Agora escolha seu segundo valor: '))
    print('')
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
