import csv
import os.path

def recebe_funcionario():
    funcionarios = []
    for c in range(3):
        funcionario = {"nome":"","cargo":"","setor":""}
        for lb in funcionario:
            print("Qual o "+lb+" do funcionário")
            funcionario[lb] = input()
        funcionarios.append(funcionario)
    return funcionarios

def registra_arquivo(cabecalho,funcionarios):
    existe = os.path.exists("funcionarios.csv")
    arquivo = open("funcionarios.csv","a+")
    with arquivo as csvfile:
        arquivo = csv.DictWriter(csvfile, delimiter=";",fieldnames=cabecalho)
        if not existe:
            arquivo.writeheader()    
        for fun in funcionarios:
            arquivo.writerow(fun) 

def exibi_arquivo():
    arquivo_novo = open("funcionarios.csv","r")
    for linha in arquivo_novo:
        print(linha,end="")

def exibi_menu_principal():
    print("==============BARATAS CROCANTES SA==============")
    print("|----------------------------------------------|")
    print("|---FUNCIONARIOS(1)----CARGO(2)-----SETOR(3)---|")
    print("|----------------------------------------------|")