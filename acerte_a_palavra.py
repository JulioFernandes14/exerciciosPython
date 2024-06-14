palavra = "Python"
letras_salvas = ''
palavra_jogada = '*'*len(palavra)
qtd_tentativas = 0

print("Bem vindo ao jogo da palavra secreta!")

while True:
    print("_"*60)
    print(f"Palavra:{palavra_jogada}")
    palavra_jogada = ''
    letra = input("Digite uma letra: ")
    
    if len(letra) != 1:
        print("Você deve digitar um caractér!")
        continue
    qtd_tentativas += 1
    
    if letra.lower() in palavra.lower():
        print (f"Parabéns! {letra} encontrada na palavra!")
        letras_salvas += letra.lower()
    else:
        print(f"{letra} não encontrada na palavra :(")
    
    for char in palavra:
        if char.lower() in letras_salvas:
            palavra_jogada += char
        else:
            palavra_jogada += "*"
    if palavra_jogada == palavra:
        print(f"Parabéns!! A palavra era:{palavra}, você acertou em {qtd_tentativas} tenttivas")
        break
        
        
        
        
        