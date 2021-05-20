print("================== Teste de dopping =================")

nome = "" 
tx = 0 

print("Qual o nome do atleta?")
nome = input()
print("Qual a taxa de testosterona do atleta?")
tx = int(input())
print("___________________________________________________________")
if tx >=1400:
	print("O atleta não passou no teste de dopping")
else:
	print("O atleta passou no teste de dopping")