#Crie um algoritmo em Python, que receba 10 notas de alunos em um vetor e retorne a média da notas, a maior nota e a menor nota.
print("==========NOTAS============")
print()

nome = []
n1 = []
n2 = []
media = []

for c in range(2):
    print("Informe o nome do ",c+1,"° aluno: ")
    nome.append(input())
    print("Informa a primeira nota do aluno ", nome[c])
    n1.append(float(input()))
    print("Informe a segunda nota do aluno ", nome[c])
    n2.append(float(input()))
   
    
for c in range(2):
     media.append = (n1[c] + n1[c]) / 2

     print("Média: ",media)
