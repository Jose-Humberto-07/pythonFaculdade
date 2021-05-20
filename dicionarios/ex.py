print("Turma")
turma = []
for l in range(5):
    aluno = []
    print("Informações do ",l+1,"° aluno: ")
    print("Informe o nome: ")
    aluno.append(input())
    print("Informe a nota da AP1: ")
    aluno.append(float(input()))
    print("Informe a nota da Ap2: ")
    aluno.append(float(input()))
    print(aluno)
    turma.append(aluno)



for aluno in turma:
    aluno = ["Gildésio", 6.4, 9.4]
    print("Nome: ",aluno[0])
    print("AP1: ",aluno[1])
    print("AP2: ",aluno[2])
