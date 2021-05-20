def inverter(texto):
    return texto[::-1]


pessoas = []

for p in range(3):
    perguntas = {"Qual o seu nome?":"",
                "Em que cidade você mora?":"",}
    print((p+1),"° entrevistado")
    for pe in perguntas:
        print(pe)
        perguntas[pe] = input()
        print()
    pessoas.append(perguntas)


for p in pessoas:
    print(p)
