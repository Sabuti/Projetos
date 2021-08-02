print('')
print('Você está usando Conversão de Temperaturas')
print('Celsius, Kelvin ou até Fahrenheit')
print('')
escolha_1 = input('De qual medida de temperatura você quer sair? ')
print('')
escolha_2 = input('Para qual medida você gostaria de saber? ')
escolha_1 = escolha_1.lower()
escolha_2 = escolha_2.lower()
if escolha_1 == 'kelvin' and escolha_2 == 'celsius':
    kelvin = int(input('Qual seu valor inicial em Kelvin? '))
    celsius = kelvin - 273.15
    print('Sua temperatura em Celsius é {}'.format(celsius))
if escolha_1 == 'kelvin' and escolha_2 == 'fahrenheit':
    kelvin = int(input('Qual seu valor inicial em Kelvin? '))
    fahrenheit = (kelvin-273.15)/1.8+32
    print('Sua temperatura em Fahrenheit é {}'.format(fahrenheit)) 
if escolha_1 == 'celsius' and escolha_2 == 'kelvin':
    celsius = int(input('Qual seu valor inicial em Celsius? '))
    kelvin = celsius + 273.15
    print('Sua temperatura em Kelvin é {}'.format(kelvin))
if escolha_1 == 'celsius' and escolha_2 == 'fahrenheit':
    celsius = int(input('Qual seu valor inicial em Celsius? '))
    fahrenheit = (celsius/1.8) + 32
    print('Sua temperatura em Fahrenheit é {}'.format(fahrenheit)) 
if escolha_1 == 'fahrenheit' and escolha_2 == 'celsius':
    fahrenheit = int(input('Qual seu valor inicial em Fahrenheit? '))
    celsius = (fahrenheit-32)/1.8
    print('Sua temperatura em Celsius é {}'.format(celsius))
if escolha_1 == 'fahrenheit' and escolha_2 == 'kelvin':
    fahrenheit = int(input('Qual seu valor inicial em Fahrenheit? '))
    kelvin = (fahrenheit-32)/1.8 + 273.15
    print('Sua temperatura em Kelvin é {}'.format(kelvin))