idades = [16,14,31,22,48,31]
idades.append(26)
print(idades)
#idades[1] = 56
#print(idades)
#idades.remove(31)
#print(idades)
#idades.pop(3)
#print(idades)
#idades.clear()
idades.insert(0,38)
print(type(idades))
print(idades)
idades.sort(reverse=True)
print(idades)
print("maior:",idades[0])
print("3 maiores:",idades[0:3])
idades.sort()
print(idades)
print("menor:",idades[0])
print("3 menores:",idades[0:3])