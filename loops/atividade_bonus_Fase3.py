"""
Construa um algoritmo em Python que receba um valor inicial e um valor final e exiba todos os números pares entre eles.
"""
print("=============")
print("VALORES PARES")
print("=============")

print()

print("De qual número você quer começar? ")
cont = int(input())
print("Em qual número você quer terminar? ")
num = int(input())


for cont in range(cont, num):
    if (cont % 2 == 0):
        print("O número ",cont," é par.")
    elif (cont % 2 != 0):
        print("O número ",cont," é ímpar.")


print("Muito obrigado, se precisar estamos aqui, volte sempre.")