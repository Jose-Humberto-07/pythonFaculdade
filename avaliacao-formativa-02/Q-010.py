print("========Lista de Dicionário Aluno==========")
turma = []
for i in range(4):
    aluno = {"nome":"","curso":"","AP1":0.0,"AP2":0.0}
    print(i+1,"º Aluno")
    for c in aluno:
        print("Qual o(a)",c,"do aluno?")
        if c in ["AP1","AP2"]:
            aluno[c] = float(input())
        else:
            aluno[c] = input()        
    aluno["média"] = (aluno["AP1"]+aluno["AP2"])/2
    turma.append(aluno)
    print()
print("==========================================")
for aluno in turma:
    for c in aluno:
        print(c+":",aluno[c])
    print()