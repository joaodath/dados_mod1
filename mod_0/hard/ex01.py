# Faça um programa, que receba as dimensões de um terreno retangular 
# (largura e comprimento) e mostre a área do terreno:

while True:
  try:
    largura = float(input("Digite a largura do terreno: "))
    if largura <= 0:
      raise ValueError('A largura deve ser maior que 0.')
    comprimento = float(input("Digite o comprimento do terreno: "))
    if comprimento <= 0:
      raise ValueError('O comprimento deve ser maior que 0.')
    break
  except ValueError:
    print('''
    Valor inválido. O valor deve ser maior que 0 no formato 42 ou 3.14.
    Tente novamente.
    ''')
    continue

area_terreno = largura * comprimento
print(f'A área do terreno é {area_terreno} m².')