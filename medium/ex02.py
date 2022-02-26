# Faça um script que peça um valor e mostre na tela se o valor é 
# positivo ou negativo e implemente a funcionalidade de não aceitar o número 0.

while True: 
  try:
    valor_para_checar= int(input("Digite o valor para ser checado: "))
    if valor_para_checar == 0:
      raise ValueError('O valor 0 não é permitido.')
    break
  except ValueError:
    print('''
    Valor inválido. O formato é -42 ou 42.
    Tente novamente.
    ''')
    continue

if valor_para_checar > 0:
  print('O valor é positivo.')
else:
  print('O valor é negativo.')