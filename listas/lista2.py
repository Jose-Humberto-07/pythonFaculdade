texto = "Tafarel cleonir demosteses sibila"
lista = texto.split()
listaNova = []

for item in lista:
    listaNova.append(item.capitalize())
#capitalize = deixar 1° letra maiúscula

print(texto)
print(lista)
print(listaNova)
print(",".join(listaNova))