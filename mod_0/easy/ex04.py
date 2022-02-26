#Faça um programa de cadastro de clientes que mostre um menu de opções e 
# permita com que a pessoa escolha umas das opções, 
# exibindo qual foi a opção escolhida.

while True: 
  try:
    print(f'''
    ===== MENU DE CLIENTES =====
    Selecione uma das opções abaixo:

    1 - Cadastrar cliente
    2 - Listar clientes
    3 - Sair

    ''')

    chosenOption = int(input("Digite a opção desejada: "))
  
  # Tratamento do erro de valor inválido
  except ValueError:
    print("Opção inválida. Digite apenas números.")
    continue
  
  ## checa qual foi a opção escolhida
  match chosenOption:
    case 1:
      print("Cadastro de cliente")
      break
    case 2:
      print("Listar clientes")
      break
    case 3:
      print("Sair")
      break
    case _:
      print("Opção inválida. Tente novamente.")
      continue ## volta para o início do loop

