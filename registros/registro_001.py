class Aluno:
    nome = ""
    n1 = 0.0
    n2 = 0.0
    media = 0.0
    aprovado = False


turma = []
for c in range(1):
    estudante = Aluno()
    print(c+1,"° Aluno")
    print("Informe o nome do aluno: ")
    estudante.nome = input()
    print("Informe a primeira nota do aluno: ")
    estudante.n1 = float(input())
    print("Informe a segunda nota do aluno: ")
    estudante.n2 = float(input())
    estudante.media = (estudante.n1 + estudante.n2) / 2
    turma.append(estudante)
    print()

for aluno in turma:
    print("======================================")
    print("Nome: ",estudante.nome,end=" | ")
    print("N1: ",estudante.n1,end=" | ")
    print("N2: ",estudante.n2,end=" | ")
    print("Média: ",estudante.media,end=" | ")
    print("Status: ",end=" ")
    if (estudante.media <= 7):
        print("Aprovado")
    else:
        print("False")


