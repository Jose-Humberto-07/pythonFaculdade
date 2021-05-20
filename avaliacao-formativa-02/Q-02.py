'''
Construa um algoritmo em Python que receba o nome e a idade de um atleta, retornando 
a categoria do mesmo conforme as sguintes condições: 11 até 13, “Juvenil 1”; 14 até 17, 
“Juvenil 2”; apartir de 18, “Adulto”; para idade menores que 11, deve ser exibida a 
mensagem “Você ainda é muito jovem, tente no próximo ano.

'''

print("Informe o seu nome: ")
nome = input()
print("Informe sua idade: ")
idade = int(input())

if idade >= 11 and idade <= 13:
    print("Juvenil 1")
elif (idade >= 14 and idade <= 17):
    print("Juvenil 2")
elif idade > 18:
    print("Adulto")
elif idade < 11:
    print("Você é muito jovem, tente próximo ano, volte sempre.")
