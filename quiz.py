# Exercício - sistema de perguntas e respostas
import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0
for questao in perguntas:
    
    while True:
        print(questao['Pergunta'])
        
        for opcao in questao['Opções']:
            print(opcao)
        resposta_usuario = input('Sua resposta: ')
        
        os.system('clear')
        
        if resposta_usuario not in questao['Opções']:
            print('Resposta inválida, tente novamente!')
            continue
        break
    if resposta_usuario == questao['Resposta']:
        acertos += 1
print(f'Quiz finalizado!\nAcertos: {acertos}/3')




