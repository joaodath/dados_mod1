# Faça um programa que peça dois números, imprima o maior deles ou 
# imprima "Números iguais" se os números forem iguais.

while True: 
  try:
    valor01 = float(input("Digite o valor 01 para ser checado: "))
    valor02 = float(input("Digite o valor 02 para ser checado: "))
    break
  except ValueError:
    print('''
    Valor inválido. O formato é -42 ou 42 ou 3.14.
    Tente novamente.
    ''')
    continue

if valor01 > valor02: 
  print(f'O valor 01 {valor01} é maior que o valor 02 {valor02}.')
elif valor01 < valor02:
  print(f'O valor 02 {valor02} é maior que o valor 01 {valor01}.')
else:
  print('Os valores são iguais.')