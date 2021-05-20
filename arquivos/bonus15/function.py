'''
Construa um algoritmo em Python que receba os dados de 10 pacientes em uma lista (vetor). Cada paciente será representado por um dicionário com as chaves: nome, idade, peso e altura. Em seguida o algoritmo deve calcular o IMC do paciente (peso/altura**2) e inserir esse IMC no mesmo dicionário. Cada paciente então deve ser inserirdo na lista. Por a lista deve ser adicionada a um arquivo .csv.
'''
import csv
import os.path

pacientes = []
cabecalho = ["nome", "idade", "peso", "altura", "imc"]

def recebePaciente():
    for c in range(10):
        print("Informe os dados do ",(c+1),"° paciente: ")
        paciente = {
            "nome":"",
            "idade":0,
            "peso":0.0,
            "altura":0.0,
            "imc":0.0
        }
        for i in paciente:
            print(i+" do paciente? ")
            if i == "imc":
                paciente["imc"] = round((paciente["peso"] / paciente["altura"] ** 2),)
                print(paciente["imc"])
            elif isinstance (paciente[i],float):
                paciente[i] = float(input())
            else:
                paciente[i] = input()
        pacientes.append(paciente)
    return pacientes

def registraArquivo():
     existe = os.path.exists("bonus15\pacientes.csv")
     arquivo = open("bonus15\pacientes.csv","a+")
     with arquivo as csvfile:
            arquivo = csv.DictWriter(csvfile, delimiter=";",fieldnames=cabecalho)
            if not existe:
                arquivo.writeheaader()
            for paciente in pacientes:
                arquivo.writerow(paciente)

def exibeArquivos():
    arquivoNovo = open("bonus15\pacientes.csv","r")
    for linha in arquivoNovo:
        print(linha,end="")

def menuPrincipal():
    print("==================================")
    print("=======CADASTRO DE PACIENTES========")
    print("==================================")
    print("Digite 1 para cadastrar pacientes ou digite qualque número para sair")