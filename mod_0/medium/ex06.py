# Crie um programa onde o usuário possa digitar vários valores numéricos e 
# cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será 
# adicionado. No final, serão exibidos todos os valores únicos digitados, 
# em ordem crescente.

continuar_adicionando = True
valores_adicionados = []
while continuar_adicionando == True:
  while True:
    try:
      valor_para_adicionar = float(input("Digite o valor para ser adicionado: "))
      break
    except ValueError:
      print(f'O valor informado {valor_para_adicionar} é inválido.')
      continue
  if valor_para_adicionar in valores_adicionados:
    print(f'O valor {valor_para_adicionar} já foi adicionado.')
  else:
    valores_adicionados.append(valor_para_adicionar)
    print(f'O valor {valor_para_adicionar} foi adicionado com sucesso.')
  
  continuar_adicionando_pergunta = input('Deseja adicionar mais um valor? (s/n) ')
  if continuar_adicionando_pergunta == 's':
    continuar_adicionando = True
    continue
  else:
    continuar_adicionando = False
    print(f'''
    Estes foram os valores adicionados:
    {valores_adicionados}
    ''')
  
  