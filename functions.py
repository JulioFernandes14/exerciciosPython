# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicador(*args):
    total = 1

    for num in args:
        total *= num
    return total
multiplicacao = multiplicador(10,2,3,4,5)

print(multiplicacao)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(numero):
    if numero%2 == 0:
        return 'Par'
    return 'Ímpar'
numero_usuario = 1

print(par_impar(numero_usuario))