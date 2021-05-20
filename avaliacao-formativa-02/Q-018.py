'''
18 º Construa um algoritmo em Python que receba o salário de 10 atletas de uma equipe de futsal em uma matriz 2x5, onde os 5 primeiros são titulares e os 5 últimos são reservas. Em seguida retorne a soma e a média dos salários da equipe titular e da equipe reserva separadamente.
'''

#import random
print("============Salário por Equipe=============")
salarios = [["TITULAR"],["RESERVA"]]
for l in salarios:
    print("Equipe: "+l[0])
    soma = 0.0
    for c in range(1,6):
        print("Qual o salario do ",c,"º atleta?")
        l.append(float(input()))
#        l.append(round(random.uniform(1500, 1000),2))
#        print(l[c])
        soma += l[c]
    l.append(round(soma,2))

print("==========================================")
print("=============TOTAL SALARIO EQUIPE=========")
for l in salarios:
    print(l)

