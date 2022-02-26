# Você está na flor da idade?
# Defina uma variável para o valor do ano do nascimento;
# Defina uma variável para o valor do ano atual;
# Defina uma variável que calcula o valor final da idade da pessoa;
# Exiba uma mensagem final dizendo a idade da pessoa e a mensagem 
# "Você está na flor da idade".

from datetime import datetime

ano_nascimento = 0
ano_atual = datetime.now().year

#este bloco de código serve para verificar se o usuário digitou um valor válido
while True: 
  try:
    ano_nascimento = int(input("Digite o seu ano de nascimento: "))
    break
  except ValueError:
    print("Ano inválido. Tente novamente.")
    continue

idade_atual = ano_atual - ano_nascimento
print(f'Voce tem {idade_atual} anos e está na flor da idade.')