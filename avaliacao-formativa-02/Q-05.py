#import random
print("============Média de Idade Funcionários==============")
idade = []
soma = 0
for c in range(90):
    print("Qual a idade do",c+1,"º funcionário?")
    idade.append(int(input()))
#   idade.append(random.randint(16, 90))
#   print(idade[c])
    soma += idade[c]
media = round(soma/len(idade),0)
print("==========================================")
print("Média da Idade:",media)