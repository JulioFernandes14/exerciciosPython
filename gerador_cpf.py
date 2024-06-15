import random

# gerador de cpf

cpf=''

for i in  range(1,10):
    
    if i == 4 or i == 7:
        cpf +='.'
    cpf +=  str(random.randint(0,9))

digitos9 = ''.join(cpf[0:11].split('.'))

# Verificação primeiro dígito
i = 10
res1 = 0

for digito in digitos9:
    res1 += int(digito) * i
    i -= 1
res1 = (res1*10)%11

digito1 = res1 if res1 <= 9 else 0

#Verificação segundo dígito
digitos9 += str(digito1)

i = 11
res2 = 0

for digito in digitos9:
    res2 += int(digito) * i
    i -= 1
res2 = (res2*10)%11
digito2 = res2 if res2 <= 9 else 0

cpf += '-' + str(digito1) + str(digito2)

print(f'CPF Gerado: {cpf}')


