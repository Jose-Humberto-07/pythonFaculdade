
#funcao
def media(ap1, ap2):
    m = (ap1 + ap2) / 2
    return m



nome = []
ap1 = []
ap2 = []

print("===============controle de notas=============")

#=[0,1,2,3,4,5]

for c in range(3): 
    print("Qual o nome do ",(c+1),"° aluno? ")
    nome.append(input())
    print("Qual a nota AP1 do " + nome[c])
    ap1.append(float(input()))
    print("Qual a nota AP2 do " + nome[c])
    ap2.append(float(input()))
    print()
    print("-------------------------------------------------------")
    print()



print("===============================================================")


for c in range(3):
    media = media(ap1[c], ap2[c])
    print("Nome: " + nome[c])
    print("Primeira nota (AP1): " , ap1[c])
    print("Segunda nota (AP2): " , ap2[c])
    print("Média: " , media) 


