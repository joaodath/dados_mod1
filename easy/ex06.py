# Qual o valor do troco?
# Defina uma variável para o valor de uma compra que custou R$100,98;
# Defina uma variável para o valor que o cliente pagou R$150,00;
# Defina uma variável que calcula o valor do troco e exiba-o no console 
# com o valor final arredondado.

valor_compra = valor_pago = valor_troco = 0.0

while True:
  try:
    valor_compra = float(input("Digite o valor da compra: R$ "))
    break

  except ValueError:
    print("Valor inválido. Tente novamente.")
    continue

while True:
  try:
    valor_pago = float(input("Digite o valor pago: R$ "))
    break

  except ValueError:
    print("Valor inválido. Tente novamente.")
    continue

valor_troco = valor_pago - valor_compra

print(f'''
Valor de uma compra R$ {valor_compra:.2f}
Valor pago R$ {valor_pago:.2f}
Valor do troco R$ {valor_troco:.2f}
''')