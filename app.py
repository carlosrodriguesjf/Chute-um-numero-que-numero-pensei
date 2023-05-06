# PROJETO 3 - PYTONISTA AUTODIDATA - CHUTE O NÚMERO: QUE NÚMERO EU PENSEI?

import random
import os

jogo = 's'

os.system('cls') or None

input('Aperte enter para começar... ')

while jogo == 's':

    numero_sorteado = random.randint(1,100)
    print('Foi gerado um número entre 1 e 100... ')
    print(numero_sorteado)

    while True:

        try:
            numero_chutado = int(input('Chute um número de 1 a 100: '))
            
        except ValueError:
            print('Digite apenas números')
            numero_chutado = int(input('Chute um número de 1 a 100: '))

        if numero_sorteado == numero_chutado:
            print('PARABÉNS! VOCÊ CHUTOU O VALOR CERTO: ' + str(numero_sorteado))
            jogo = input('Jogo encerrado, gostaria de jogar novamente? (s/n)')
            os.system('cls') or None
            break

        elif numero_chutado > numero_sorteado:
            print('Chute um número menor')

        else:
            print('Chute um número maior')
    

print(50*'-')
print('Encerrando o jogo...')
print(50*'-')



