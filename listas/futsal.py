
"""Construa um algoritmo em Python que receba o salario de jogares de um time de futsal em duas listas. Lista T, com o salário dos 5 titulares e lista R, com o salário dos 5 reservas.Em seguida retorne a soma, a média, o maior salário e o menor salário. Todas as informações devem ser discriminadas para time reserva, time titular e geral.
"""
import random

print("FUTSAL")

titular = [1234.34, 11234.234, 345345, 34345, 534534]
reserva = [2234,234,234,2345,56567,]
geral = titular + reserva
soma = 0.0
media = 0.0
maior = 0.0
menor = 0.0
somaR = 0.0
mediaR = 0.0





for i in range(5):
    soma+= titular[i]
    media = soma / len(titular)

    if (titular[i] > maior):
        maior = titular[i]

    if (titular[i] < maior):
        menor = titular[i]   



print("============TITULARES==========")
print("Menor salário: " , menor)
print("Maior salário: " , maior)
print("Média de salários: " , media)
print("total: " , soma)
print
print("============TITULARES==========")
print("Menor salário: " , menor)
print("Maior salário: " , maior)
print("Média de salários: " , media)
print("total: " , soma)
print
print("============GERAL==========")
print("Menor salário: " , menor)
print("Maior salário: " , maior)
print("Média de salários: " , media)
print("total: " , soma)
print()
