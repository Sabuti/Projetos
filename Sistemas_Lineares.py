opcoes_todos = ['Sim','sim','S','s','Não','Nao','não','nao','N','n']
posicoes_2 = ['a11','a12','a21','a22']
posicoes_3 = ['a11','a12','a13','a21','a22','a23','a31','a32','a33']
valores,lista_incognitas_1,lista_incognitas_2,lista_incognitas_3 = [],[],[],[]
incognitas = ['x','y','z']
dois, tres, sistema_2, sistema_3,i = 0,0,0,0,0
print('--------------------------------------------')
print('Bem Vindo ao Calculos com Sistemas Lineares!')
print('-------------------------------------------- \n')
escolha_determinantes = input('Gostaria de calcular determinantes? ')
while escolha_determinantes not in opcoes_todos:
    print('Por favor, apenas aceitamos sim, não e seus relacionados como resposta')
    escolha_determinantes = input('Gostaria de calcular determinantes? ')
if escolha_determinantes in opcoes_todos[:4]:
    print('Ok, bora calcular isso')
    tamanho_matriz = int(input('Qual o tamanho da sua matriz? '))
    if tamanho_matriz == 2:
        while dois < len(posicoes_2):
            valor = int(input(f'Qual seu {posicoes_2[dois]}? '))
            valores.append(valor) 
            dois += 1
        valor_det = valores[0] * valores[3] - valores[1] * valores[2]
        print(f'Sua determinante de matriz 2 é {valor_det} \n')
    elif tamanho_matriz == 3:
        while tres < len(posicoes_3):
            valor = int(input(f'Qual seu {posicoes_3[tres]}? '))
            valores.append(valor) 
            tres += 1
        valores_positivos = valores[0] * valores[4] * valores[8] + valores[1] * valores[5] * valores[6] + valores[2] * valores[3] * valores[7]
        valores_negativos = valores[2] * valores[4] * valores[6] + valores[0] * valores[5] * valores[7] + valores[1] * valores[3] * valores[8]
        valor_det = valores_positivos - valores_negativos
        print(f'Sua determinante de matriz 3 é {valor_det} \n')
    else:
        print('Por enquanto apenas temos de 2 e de 3...')
achar_incognitas = input('Quer que eu encontre as incógnitas do seu problema? ')
print('Nota, apenas ajudo com problemas matemáticos, qualquer outro problema fica na sua mão')
while achar_incognitas not in opcoes_todos:
    print('Por favor, apenas aceitamos sim, não e seus relacionados como resposta')
    achar_incognitas = input('Quer que eu veja qual a classificação do seu problema? ')
if achar_incognitas in opcoes_todos[:4]:
    print('Ok, deixa comigo! \n')
    opcao_sistema = int(input('É um sistema com 2 ou 3 incógnitas? '))
    letra = input('Qual sua letra de incógnita? ')
    if opcao_sistema == 2:
        while sistema_2 < len(incognitas[:2]):
            print('Sobre a função 1')
            valor1 = input(f'Qual seu {incognitas[sistema_2]}? ')
            lista_incognitas_1.append(valor1) 
            print('Agora sobre a função 2')
            valor2 = input(f'Qual seu {incognitas[sistema_2]}? ')
            lista_incognitas_2.append(valor2) 
            sistema_2 += 1
        if lista_incognitas_1[0] == letra:
            valor_k = int(lista_incognitas_2[0])*int(lista_incognitas_1[1])/int(lista_incognitas_2[1])
            print(f'\n k vai tem que ser diferente de {valor_k} pra ser SPD')
            print(f'Se k = {valor_k} vai ser SI ou SPI')
        if lista_incognitas_1[1] == letra:
            valor_k = int(lista_incognitas_2[1])*int(lista_incognitas_1[0])/int(lista_incognitas_2[0])
            print(f'\n k vai tem que ser diferente de {valor_k} pra ser SPD')
            print(f'Se k = {valor_k} vai ser SI ou SPI')
        if lista_incognitas_2[0] == letra:
            valor_k = int(lista_incognitas_2[1])*int(lista_incognitas_1[0])/int(lista_incognitas_1[1])
            print(f'\n k vai tem que ser diferente de {valor_k} pra ser SPD')
            print(f'Se k = {valor_k} vai ser SI ou SPI')
        if lista_incognitas_2[1] == letra:
            valor_k = int(lista_incognitas_2[0])*int(lista_incognitas_1[1])/int(lista_incognitas_1[0])
            print(f'\nk vai tem que ser diferente de {valor_k} pra ser SPD')
            print(f'Se k = {valor_k} vai ser SI ou SPI')
    elif opcao_sistema == 3:
        valores.clear()
        while sistema_3 < len(incognitas):
            print('Sobre a função 1')
            valor1 = input(f'Qual seu {incognitas[sistema_3]}? ')
            valores.append(valor1) 
            print('Agora sobre a função 2')
            valor2 = input(f'Qual seu {incognitas[sistema_3]}? ')
            valores.append(valor2) 
            print('Agora sobre a função 3')
            valor3 = input(f'Qual seu {incognitas[sistema_3]}? ')
            valores.append(valor3) 
            sistema_3 += 1
        while i < 9:
            if valores[i] == letra:
                pass
            else:
                valores[i] = int(valores[i])
            i += 1
        if valores[0] == letra:
            valores_positivos = valores[3] * valores[2] * valores[7] + valores[6] * valores[1] * valores[5]
            valores_negativos = valores[6] * valores[2] * valores[4] + valores[8] * valores[1] * valores[3]
            valores_m = valores[4] * valores[8] - valores[5] * valores[7]
            det = valores_positivos - (valores_negativos)
            resultado_m = -det / valores_m
        elif valores[1] == letra:
            valores_positivos = valores[0] * valores[4] * valores[8] + valores[3] * valores[7] * valores[2]
            valores_negativos = valores[6] * valores[4] * valores[2] + valores[0] * valores[7] * valores[5]
            valores_m = valores[6] * valores[5] - valores[8] * valores[3]
            det = valores_positivos - (valores_negativos)
            resultado_m = -det / valores_m
        elif valores[2] == letra:
            valores_positivos = valores[0] * valores[4] * valores[8] + valores[6] * valores[1] * valores[5]
            valores_negativos = valores[0] * valores[7] * valores[5] + valores[3] * valores[1] * valores[8]
            valores_m = valores[3] * valores[7] - valores[6] * valores[4]
            det = valores_positivos - (valores_negativos)
            resultado_m = -det / valores_m
        elif valores[3] == letra:
            valores_positivos = valores[0] * valores[4] * valores[8] + valores[6] * valores[1] * valores[5]
            valores_negativos = valores[0] * valores[7] * valores[5] + valores[6] * valores[4] * valores[2]
            valores_m = valores[2] * valores[7] - valores[1] * valores[8]
            det = valores_positivos - (valores_negativos)
            resultado_m = -det / valores_m
        elif valores[4] == letra:
            valores_positivos = valores[3] * valores[7] * valores[2] + valores[6] * valores[1] * valores[5]
            valores_negativos = valores[0] * valores[7] * valores[5] + valores[3] * valores[1] * valores[8]
            valores_m = valores[8] * valores[0] - valores[6] * valores[2]
            det = valores_positivos - (valores_negativos)
            resultado_m = -det / valores_m
        elif valores[5] == letra:
            valores_positivos = valores[0] * valores[4] * valores[8] + valores[3] * valores[7] * valores[2]
            valores_negativos = valores[2] * valores[4] * valores[6] + valores[3] * valores[1] * valores[8]
            valores_m = valores[6] * valores[1] - valores[7] * valores[0]
            det = valores_positivos - (valores_negativos)
            resultado_m = -det / valores_m
        elif valores[6] == letra:
            valores_positivos = valores[0] * valores[4] * valores[8] + valores[3] * valores[7] * valores[2]
            valores_negativos = valores[5] * valores[7] * valores[0] + valores[3] * valores[1] * valores[8]
            valores_m = valores[5] * valores[1] - valores[4] * valores[2]
            det = valores_positivos - (valores_negativos)
            resultado_m = -det / valores_m
        elif valores[7] == letra:
            valores_positivos = valores[0] * valores[4] * valores[8] + valores[6] * valores[1] * valores[5]
            valores_negativos = valores[2] * valores[4] * valores[6] + valores[3] * valores[1] * valores[8]
            valores_m = valores[3] * valores[2] - valores[5] * valores[0]
            det = valores_positivos - (valores_negativos)
            resultado_m = -det / valores_m
        else:
            valores_positivos = valores[3] * valores[7] * valores[2] + valores[6] * valores[1] * valores[5]
            valores_negativos = valores[2] * valores[4] * valores[6] + valores[0] * valores[7] * valores[5]
            valores_m = valores[0] * valores[4] - valores[3] * valores[1]
            det = valores_positivos - (valores_negativos)
            resultado_m = -det / valores_m
        print(f'\nSe {letra} != de {resultado_m}, é SPD')
        print(f'Se {letra} = {resultado_m}, é SI ou SPI')
        print('\nSe quiser descobrir se é Si ou SPI, faz escalonamento')
        print('Meu trabalho acaba por aqui')
    else:
        print('Só temos essas 2 opções, fazer o que...')