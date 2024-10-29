numero_secreto = 3
tentativas = 0
max_tentativas = 3

print('Estou pensando em um número de 0 a 5.')

while tentativas < max_tentativas:
    palpite = int(input('Digite um número de 0 a 5 para adivinhar: '))
    
    if palpite == numero_secreto:
        print('Parabéns! Você adivinhou o número!')
        break
    else:
        print('Tente novamente!')
        tentativas += 1

if tentativas == max_tentativas:
    print(f'Você errou todas as tentativas. O número era {numero_secreto}.')
