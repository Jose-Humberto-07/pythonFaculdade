sal = []
contador = 0
menor = 900
for i in range(90):
  print("Digite o salario do",i+1,"º funcionário?")
  sal.append(int(input()))
  if sal[i] < menor:
    contador += 1    
print("==========================================")
print("Quantidade de funcionarios que recebem menos de R$ 900,00: ",contador)