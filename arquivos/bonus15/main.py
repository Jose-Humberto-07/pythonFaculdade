
from bonus15.function import exibeArquivos
from bonus15.function import menuPrincipal
from bonus15.function import recebePaciente
from bonus15.function import registraArquivo

menuPrincipal()

print("O que deseja fazer? ")
op = input()

if op == "1":
    pacientes = recebePaciente()
else:
    print("Obrigado por acessar, volte sempre.")

registraArquivo()

exibeArquivos()