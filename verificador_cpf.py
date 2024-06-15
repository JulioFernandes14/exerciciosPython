cpf = '883.734.463-54'
digitosEnviados = [int(cpf[12]),int(cpf[13])]
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
digitosVerificar = [digito1,digito2]

verificacao = f'{cpf} é um CPF Válido' if digitosEnviados == digitosVerificar else f'{cpf} é um CPF Inválido'

print(verificacao)
