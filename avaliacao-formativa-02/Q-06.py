print("============Funcionários em ordem inversa==============")
nome = []
for c in range(5):
    print("Qual o nome do ",c+1,"º funcionário?")
    nome.append(input())
nome.sort(reverse=True)
print("==========================================")
for n in nome:
    print(n)