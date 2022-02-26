# Elabore um programa que escreve seu nome completo na primeira linha, 
## seu endereço na segunda e o CEP e telefone na terceira.

nomeCompleto = input("Digite seu nome completo: ")
endereco = input("Digite seu endereço: ")
cep = int(input("Digite seu CEP, apenas números: "))

print(f'''
Nome: {nomeCompleto}
Endereço: {endereco}
CEP: {cep}
''')