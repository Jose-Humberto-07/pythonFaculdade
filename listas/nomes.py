print("Nomes")

nomes = []

for i in range(10):
    print("Informe 10 nomes: ")
    nomes.append(input())


nomes.sort(reverse=True)

print(nomes)