'''
Construa um algoritmo em Python que receba os dados de 10 pacientes em uma lista (vetor). Cada paciente será representado por um dicionário com as chaves: nome, idade, peso e altura. Em seguida o algoritmo deve calcular o IMC do paciente (peso/altura**2) e inserir esse IMC no mesmo dicionário. Cada paciente então deve ser inserirdo na lista. Por a lista deve ser adicionada a um arquivo .txt.
'''

paciente = {
            "nome":"",
            "idade":0,
            "peso":0.0,
            "altura":0.0,
           
}

pacientes = []

for i in range(1):
    print(i+1,"° paciente: ")
    print("Informe o nome do paciente: ")
    paciente["nome"] = input()
    print("Informe a idade do paciente: ")
    paciente["idade"] = int(input())
    print("Informer o peso do paciente: ")
    paciente["peso"] = float(input())
    print("Informe a altura do paciente: ")
    paciente["altura"] = float(input())
    paciente["imc"] = paciente["peso"] / paciente["altura"]**2
    pacientes.append(paciente)


for paciente in pacientes:
    print("Nome: ",paciente["nome"])
    print("Idade: ",paciente["idade"])
    print("Peso: ",paciente["peso"])
    print("Altura: ",paciente["altura"])
    print("IMC: ", ["imc"])

print()
print(paciente.keys())
print(paciente.values())
print()
print(pacientes)