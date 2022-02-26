# Crie um programa em Python que peça a nota do aluno, que deve ser um real 
# entre 0.00 e 10.0
# Se a nota for menor que 6.0, deve exibir a nota F.
# Se a nota for de 6.0 até 7.0, deve exibir a nota D.
# Se a nota for entre 7.0 e 8.0, deve exibir a nota C.
# Se a nota for entre 8.0 e 9.0, deve exibir a nota B.
# Por fim, se for entre 9.0 e 10.0, deve exibir um belo de um A.


while True: 
  try:
    nota_aluno = float(input("Digite a nota do aluno: "))
    if nota_aluno < 0.00 or nota_aluno > 10.00:
      raise ValueError('Nota inválida. Deve ser um número real entre 0.00 e 10.00')
    break
  except ValueError:
    print('''
    Valor inválido. O formato é 6 ou 3.14.
    Tente novamente.
    ''')
    continue

nota_final = 'A'

# usar limite superior, <= 6.0 vira < 7.0
if nota_aluno <= 6.0:
  nota_final = 'F'
elif  nota_aluno < 7.0:
  nota_final = 'D'
elif nota_aluno < 8.0:
  nota_final = 'C'
elif nota_aluno < 9.0:
  nota_final = 'B'
elif nota_aluno <= 10.0:
  nota_final = 'A'
else:
  nota_final = 'Nota inválida.'

print(nota_final)
