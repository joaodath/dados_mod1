# Agora, imprima todas as tabuadas do número 1 ao 10.

for tabuada in range(1, 11):
  for numero in range(1, 11):
    print(f'|| {tabuada} x {numero} = {tabuada * numero} ||')
    if numero == 10:
      print('=' * 15)