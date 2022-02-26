# Faça um programa que pergunte ao usuário um número e valide se o numero é 
# par ou impar:
# Crie uma variável para receber o valor, com conversão para inteiro
# Para um número ser par, a divisão dele por 2 tem que dar resto 0

while True: 
  try:
    valor_para_checar= int(input("Digite o valor para ser checado: "))
    break
  except ValueError:
    print('''
    Valor inválido. O formato é 42 ou 84.
    Tente novamente.
    ''')
    continue

match valor_para_checar % 2:
  case 0:
    print('O valor é par.')
  case _:
    print('O valor é impar.')