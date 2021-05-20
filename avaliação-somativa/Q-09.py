'''
Construa um algoritmo em Python que receba os dados de um cliente em um dicionário: nome, conta e renda(decimal). Em seguida o algoritmo deve calcular o Crédito do cliente (renda/3) e inserir esse Crédito no mesmo dicionário. Por fim exibir os dados do cliente.
'''

cliente = {}

print("======================================")
print("=================CONTA================")
print("======================================")

for c in range(1):
    print("Nome: ")
    cliente['nome'] = input()
    print('Conta: ')
    cliente['conta'] = input()
    print('Renda: ')
    cliente['renda'] = float(input())    
    cliente['credito'] = round((cliente['renda']/3),2)

print(cliente)