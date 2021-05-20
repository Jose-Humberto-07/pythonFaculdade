'''
Utilizando uma estrutura de repetição, construa um algoritmo em Python que receba um 
número inteiro e retorne o fatorial do mesmo. 
Ex. 4, “4 fatorial é 24.” (4!=4*3*2*1).
'''

print("=========FATORIAL=========")
print()

n = int(input("Digite um número para fatorar: "))
for i in range((n - 1), 1, -1):
   n = n * i
print("Resultado: ",n)