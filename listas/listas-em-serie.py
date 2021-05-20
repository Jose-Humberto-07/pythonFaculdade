"""
frutas = ["Maça", "Banana", "Abacate", "Morango"]
frutas.append("Açaí")
for frutas in frutas:
    print(frutas)

print()
print(frutas)
print()

print("Qual fruta deseja procurar? ")
fp = input()

if fp.lower() in frutas:
    print("Temos" + fp)
else:
    print("não tem.")    

"""

frutas = ["Maça", "Banana", "Abacate", "Morango"]
frutas += ["Açaí"]
#animal += ["Jumento"]

print(frutas)

#listas com parâmetros

def eliminaDduplicatas(lista):
    listaNova = [lista]
    for item in lista:
        if item not in listaNova:
            listaNova.append(item)
    return listaNova        


frutas = ["Maça", "Banana", "Abacate", "Morango"]
frutas += ["Açaí", "banana", "Abacate"]

print(frutas)
print(frutas = eliminaDduplicatas(frutas))