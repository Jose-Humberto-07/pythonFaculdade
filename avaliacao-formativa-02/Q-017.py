'''
17º Construa um algoritmo em Python que receba os dados de um paciente em um vetor:
nome, idade, peso e altura. Em seguida o algoritmo deve calcular o IMC do paciente (peso/altura**2) e inserir esse IMC no mesmo vetor. Por fim exibir os dados do paciente.
'''

print("============Dicionário Paciente==============")
Paciente = {"nome":"","idade":"","Peso":0.0,"Altura":0.0}
for c in Paciente:
    print("Qual o(a)",c,"do Paciente?")
    if c in ["Peso","Altura"]:
        Paciente[c] = float(input())
    else:
        Paciente[c] = input()        
Paciente["IMC"] = (Paciente["Peso"]/(Paciente["Altura"]**2))
 
print("==========================================")
for c in Paciente:
    print(c+":",Paciente[c])