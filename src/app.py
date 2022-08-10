# pylint: disable=C0103,C0114,C0115,C0116
"""
Script principal
"""
import pwinput as pw
import janela.gui as gui

palavra_secreta = pw.pwinput(prompt = 'Digite a palavra secreta: ')
chances = 3
digitadas = []

while True:
    if chances <= 0:
        print('Você perdeu!')
        break

    guess = input('Digite uma letra: ')

    if len(guess) > 1:
        print('Não vale, digite só uma letra.')
        continue

    digitadas.append(guess)

    palavra = ''

    if guess not in palavra_secreta:
        chances -= 1
        print(f'Não foi dessa vez. Você tem {chances} chances.')
        digitadas.pop()
    else:
        print('Muito bem! Você acertou!')

    for letra in palavra_secreta:
        if letra in digitadas:
            palavra += letra
        else:
            palavra += '*'

    print(palavra)

    if palavra == palavra_secreta:
        print(f'Você ganhou! A palavra era {palavra_secreta}.')
        break
