print("=========================================")
print("=========================================")
print("==================BANCO==================")
print("=========================================")
print("=========================================")


banco = []
for  i in range (2):
  cliente = {"nome":'',"conta":0.0,"renda":0.0}
  print ("===================================")
  print ("Insira os dados da ",i+1," º pessoa.")
  for reg in cliente:
    print ("Qual ",reg," da pessoa ?")
    if reg in ["conta","renda"]:
      cliente[reg] = float (input())
    else:
      cliente[reg] = input()
  cliente["credit"] = round((cliente["renda"]/3),2)
  banco.append(cliente)
  print()

print ("===========================")
for cliente in banco:
  for reg in cliente:
    print (reg+":",cliente[reg])
  print()