# Faça um programa que vai receber como parâmetro o ano de nascimento de 
# uma pessoa, retornando um valor literal indicando se uma pessoa tem 
# voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições:

from datetime import datetime

ano_atual = datetime.now().year
ano_nascimento = 0

while True:
  try:
    ano_nascimento = int(input("Digite o seu ano de nascimento: "))
    if ano_nascimento >= ano_atual:
      raise ValueError('O ano de nascimento deve ser maior que o ano atual.')
    break
  except ValueError:
    print(f'''
    Valor inválido. O ano de nascimento deve ser maior que o 
    ano atual {ano_atual} no formato '2022'.
    Tente novamente.
    ''')
    continue

idade_usuario = ano_atual - ano_nascimento

if idade_usuario < 16:
  print('Voto NEGADO.')
elif idade_usuario >= 16 and idade_usuario < 18 or idade_usuario > 65:
  print('Voto OPCIONAL.')
else:
  print('Voto OBRIGATÓRIO.')