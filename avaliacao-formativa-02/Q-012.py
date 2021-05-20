print("================== Alturas =================")

nome = "" 
altura = 0.00 
sexo = ""

print("Qual o nome da pessoa a ser analisada?")
nome = input()
print("Qual o sexo dela? M ou F")
sexo = input()
sexo = sexo.upper()
print("Qual a altura dela?(em metros)")
altura = float(input())


print("___________________________________________________________")
print()

if sexo == "F":
	if altura < 1.60:
		print(nome,"é baixa, pois tem menos de 1,60M")
	elif altura < 1.71:
		print(nome,"tem uma altura media, pois tem até de 1,70M e é maior que 1,60M")	
	else:
			print(nome,"é alta, pois tem mais de 1,70M")
elif sexo == "M":
	if altura < 1.66:
		print(nome,"é baixo, pois tem menos de 1,60M")
	elif altura < 1.79:
		print(nome,"tem uma altura media, pois tem até de 1,70M e é maior que 1,60M")	
	else:
			print(nome,"é alto, pois tem mais de 1,70M")
