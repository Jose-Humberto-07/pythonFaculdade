import csv
import os.path
existe = os.path.exists("funcionarios.csv")

arquivo = open("funcionarios.csv","a+")
cabecalho = ["nome","cargo","setor"]
funcionarios = []

for c in range(3):
    funcionario = {"nome":"","cargo":"","setor":""}
    for lb in funcionario:
        print("Qual o "+lb+" do funcionário")
        funcionario[lb] = input()
    funcionarios.append(funcionario)

with arquivo as csvfile:
    arquivo = csv.DictWriter(csvfile, delimiter=";",fieldnames=cabecalho)
    if not existe:
        arquivo.writeheader()    
    for fun in funcionarios:
        arquivo.writerow(fun)  
arquivo_novo = open("funcionarios.csv","r")
for linha in arquivo_novo:
    print(linha,end="")