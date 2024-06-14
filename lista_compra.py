import os

lista = []

while True:

    acao = input('Digite [i]nserir [a]pagar [l]istar: ').lower()

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    if acao == 'i':
        item = input('Digite o item a ser adicionado: ')
        lista.append(item)
    elif acao == 'a':
        indice = input('Digite o índice do item para apagar: ')
        try:
            lista.pop(int(indice))
        except:
            print("Índice inválido!")
    elif acao == 'l':
        if len(lista) > 0:
            for indice,produto in enumerate(lista):
                print (indice,item)
        else:
            print('Lista vazia')
    else:
        print('Ação inválida')