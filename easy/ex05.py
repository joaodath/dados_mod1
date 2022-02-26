# E os 10% do garçom?
# Defina uma variável para o valor de uma refeição que custou R$ 42,54;
# Defina uma variável para o valor da taxa de serviço que é de 10%;
# Defina uma variável que calcula o valor total da conta e exiba-o no console 
# com essa formatação: R$ 9999.99.

while True:
  try:
    valor_refeicao = float(input("Digite o valor da refeição: "))
    break

  except ValueError:
    print("Valor inválido. Tente novamente.")
    continue

taxa_servico = 0.1

valor_total = valor_refeicao + (valor_refeicao * taxa_servico)

print(f'''
Valor da Refeição: R$ {valor_refeicao:.2f}
Valor da Taxa de Serviço: {taxa_servico * 100}%
Valor total: R$ {valor_total:.2f}
''')