''''
Utilizando uma estrutura de repetição, construa um algoritmo em Python que receba a 
altura de 50 atletas e informe a maior altura.
'''

import random
print("============Atleta Mais Alto==============")
altura = []
for c in range(50):
    print("Qual a altura do",c+1,"º atleta? (em metros)")
    altura.append(float(input()))
#   altura.append(round(random.uniform(1.4, 2.4),2))
#   print(altura[c])

altura.sort(reverse=True)
print("==========================================")
print("Maior altura:",altura[0])
