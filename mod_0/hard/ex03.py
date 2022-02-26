# Jogo da adivinhação: Escreva um programa que faça o computador “pensar” em
# um número inteiro entre 0 e 10 e peça para o usuário tentar descobrir qual 
# foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

continuar_jogando = True #controla o loop do jogo

while continuar_jogando == True:
  numero_secreto = randint(0, 10)
  while True:
    print(f'''
    Eu pensei em um número entre 0 e 10.
    Você consegue adivinhar qual foi?
    ''')

    try:
      numero_usuario = int(input('Digite o número: '))
      if numero_usuario > 10 or numero_usuario < 0:
        raise ValueError('Número inválido. Tente novamente.')
      if numero_usuario == numero_secreto:
        print('Parabéns! Você acertou.')
        break
      else:
        print(f'Você errou. O número secreto era {numero_secreto}.')
        break
    except ValueError:
      print('''
      Valor inválido. Tente novamente.
      Lembre-se: o número que eu pensei está entre 0 e 10.''')
      continue
  continuar_jogando = input('Deseja continuar jogando? [S/N] ')
  if continuar_jogando.upper() == 'S':
    continuar_jogando = True
    continue
  else:
    continuar_jogando = False
    break