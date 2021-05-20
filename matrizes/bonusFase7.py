'''
Construa um algoritmo em Python que receba o salário de 15 funcionários  em uma matriz 3x5, onde os 5 primeiros são do setor de RH, os 5 próximos da área de TI e os 5 últimos são do setor de Marketing. Em seguida retorne a soma dos salários das equipes de RH, TI e Marketing.

'''
matriz = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
soma = 0;



for l in range(0,3):
    for c in range(0,5):
        matriz[l][c] = float(input("digite o salário: "))


for l in range(0,3):
    for c in range(0,5):
        soma += matriz[l][c] 

       
print("Total: ", soma)