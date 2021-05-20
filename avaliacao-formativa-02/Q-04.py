print("============Funcionários por Sexo==============")
nome = []
sexo = []
cont_m = 0
cont_f = 0
for c in range(5):
    print("Qual o nome do ",c+1,"º funcionário?")
    nome.append(input())
    print("Qual o sexo do ",c+1,"º funcionário? (M ou F)")
    sexo.append(input())
    if sexo[c] == "F":
        cont_f += 1
    else:
        cont_m += 1

print("==========================================")
print("Quantidade do sexo feminino:",cont_f)
print("Quantidade do sexo masculino:",cont_m)