# Conversor de moedas: Crie um programa que solicite um um valor em real 
# ao usuário e converta esse valor, para:
# DOLAR
# EURO
# LIBRA ESTERLINA
# DÓLAR CANADENSE
# PESO ARGENTINO
# PESO CHILENO
# Para esse exercício você precisará realizar uma pesquisa para saber a 
# cotação de cada moeda em real. Mostrar o resultado no formato U$9999.99

#este bloco de código serve para verificar se o usuário digitou um valor válido
while True: 
  try:
    valor_em_real = float(input("Digite o valor em Real para ser convertido: R$ "))
    break
  except ValueError:
    print('''
    Valor inválido. O formato é R$ 50.00
    Tente novamente.
    ''')
    continue

#fatores de conversão referentes ao valor em R$1
dolar_usa = 0.19
dolar_canadense = 0.25
euro = 0.17
libra = 0.14
peso_argentino = 20.81
peso_chileno = 154.95

print(f'''
O valor que pediu para converter é R$ {valor_em_real:.2f}

    DOLAR USA: R$ {valor_em_real * dolar_usa:.2f}
    DOLAR CANADENSE: R$ {valor_em_real * dolar_canadense:.2f}
    EURO: R$ {valor_em_real * euro:.2f}
    LIBRA ESTERLINA: R$ {valor_em_real * libra:.2f}
    PESO ARGENTINO: R$ {valor_em_real * peso_argentino:.2f}
    PESO CHILENO: R$ {valor_em_real * peso_chileno:.2f}
''')





