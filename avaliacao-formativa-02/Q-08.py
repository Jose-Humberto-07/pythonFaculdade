#import random
print("============Salário por Setor=============")
salarios = [["RH"],["TI"],["MKT"]]
for l in salarios:
    print("Setor: "+l[0])
    soma = 0.0
    for c in range(1,6):
        print("Qual o salario do ",c,"º funcionário?")
        l.append(float(input()))
#        l.append(round(random.uniform(1500, 1000),2))
#        print(l[c])
        soma += l[c]
    l.append(round(soma,2))

print("==========================================")
for l in salarios:
    print(l)