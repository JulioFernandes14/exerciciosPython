#Calculadora de dois números

operadores = '+-*/'

print('Bem vindo a calculadora de dois números!')
while True:
    print('_'*50)
    num1 = input('Digite o valor do primeiro número:')
    num2 = input('Digite o valor do segundo número:')
    
    try:
        num1 = float(num1)
        num2 = float(num2)
    except:
        print('Dígitação de valores inválida, tente novamente')
        print('_'*50)
        print('_'*50)
        continue
    print('_'*50)
    operador = input(' [+] para soma \n [-] para subtração \n [*] para multiplicação \n [/] para divisão \n Digite: ')
    
    if operador not in operadores:
        print('Dígitação de operador inválida, tente novamente')
        print('_'*50)
        print('_'*50)
        continue
    if operador == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operador == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    elif operador == '*':
        print(f'{num1} * {num2} = {num1 * num2}')
    elif operador == '/':
        try:
            print(f'{num1} / {num2} = {num1 / num2}')
        except:
            printf('Impossível dividir um valor por 0')
    continuar = input('Deseja realizar outro cálculo? [S]im ou [N]ão: ').lower().startswith('s')
    if continuar is not True:
        break;
print('Calculadora finalizada!')