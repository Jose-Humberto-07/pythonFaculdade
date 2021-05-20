print("================== Soma de numeros pares e impares =================")

inicial = 0
par = 0
impar = 0
final = 0

print("Qual o numero inicial?")
inicial = int(input())
print("Qual o numero final?")
final = int(input())

print("___________________________________")
print()
for c in range(inicial,final):
	if c % 2 == 0:
		print("Pares ->",par,"+",c)
		par = c + par
		print("= ->",par)
		print()

	else:
		print("Impares ->",impar,"+",c)
		impar = c + impar
		print("= ->",impar)
		print()

