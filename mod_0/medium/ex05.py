# Reajuste salarial: As empresas @.com resolveram dar um aumento de salário 
# aos seus colaboradores e lhe contrataram para desenvolver o programa que 
# calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste 
# segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5%
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

valor_salario = 0
while True: 
  try:
    valor_salario = float(input("Digite o valor a ser reajustado: "))
    if valor_salario < 0.00:
      raise ValueError('Nota inválida. Deve ser um número real entre 0.00 e 10.00')
    break
  except ValueError:
    print('''
    Valor inválido. O formato é 6 ou 3.14.
    Tente novamente.
    ''')
    continue

porcentagem_reajuste = 0

if valor_salario <= 280.00:
  porcentagem_reajuste = 20
elif valor_salario < 700.00:
  porcentagem_reajuste = 15
elif valor_salario >= 1500.00:
  porcentagem_reajuste = 5

salario_reajustado = valor_salario + (valor_salario * (porcentagem_reajuste / 100))

print(f'''
Salário antes do reajuste: R${valor_salario}
Percentual de aumento: {porcentagem_reajuste}%
Valor do aumento: R${salario_reajustado}
''')