from funcoes import *
cabecalho = ["nome","cargo","setor"]

exibi_menu_principal()
print("O que deseja acessar?")
op = input()

if op == "1":
    funcionarios = recebe_funcionario()

exibi_arquivo()