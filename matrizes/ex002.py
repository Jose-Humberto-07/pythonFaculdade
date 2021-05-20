equipes = []

for l in range(3):
    equipe = 3
    print(l+1,"ª equipe: ")
    for c in range(6):
        print("Informe o nome do ",c+1,"° membro: ")
        membro = input()
        equipe.srt(append(membro))
    equipes.append(equipe) 
    print(equipe)
cont = 1
for equipe in equipes:
    print(cont, "ª equipe: ")
    for membro in equipe:
        print(membro)
        print()
        cont += 1