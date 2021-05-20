'''Construa um algotirmo em Python, que receba o nome e o sexo de 10 usuários e retorne a Quantidade de pessoas de cada sexo.
'''
nome = []
sexo = []
totM = 0
totF = 0

for i in range(10):
    print("Informe o seu nome: ")
    nome.append(str(input()))  
    print("Informe o seu sexo: ('F' para feminino e 'M' para masculino) ")
    sexo.append(str(input())) 

    if (sexo[i] == "F"):
        totF += 1
    elif (sexo[i] == "M"):
        totM += 1

print("Pessoas masculinas: ",totM)
print()
print("Pessoas femininas: ",totF)
