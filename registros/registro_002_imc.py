'''
Construa um algoritmo em Python que receba os dados de 10 pacientes em uma lista (vetor). Cada paciente será representado por um registro com os campos: nome, idade, peso e altura. Em seguida o algoritmo deve calcular o IMC do paciente (peso/altura**2) e inserir esse IMC no mesmo registro. Cada paciente então deve ser inserirdo na lista. Por fim exibir os dados de todos os pacientes.
'''

class Paciente:
    nome = ""
    idade = 0
    peso = 0.0
    altura = 0.0
    imc = 0.0

pacientes = []
for i in range(1):
    pessoa = Paciente()
    print(i+1,"Paciente: ")
    print("Informe o nome do paciente: ")
    pessoa.nome = input()
    print("Informe a idade do paciente: ")
    pessoa.idade = int(input())
    print("Informe o peso do paciente: ")
    pessoa.peso = float(input())
    print("Informe a altura do paciente: ")
    pessoa.altura = float(input())
    pessoa.imc = pessoa.peso / pessoa.altura**2
    pacientes.append(pessoa)

for Paciente in pacientes:
    print("===============================================")
    print("Nome: ",pessoa.nome,end= "  ")
    print("Idade: ",pessoa.idade,end="  ")
    print("Peso: ",pessoa.peso,end= "  ")
    print("Altura: ",pessoa.altura,end="  ")
    print("Imc: ",pessoa.imc,end="  ")
    