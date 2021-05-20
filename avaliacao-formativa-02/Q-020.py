hospital = []
for i in range(10):
    paciente = {"Nome":"","Idade":"","Peso":0.0,"Altura":0.0}
    print(i+1,"º paciente")
    for c in paciente:
        print("Qual o(a)",c,"do paciente?")
        if c in ["Peso","Altura"]:
            paciente[c] = float(input())
        else:
            paciente[c] = input()        
    paciente["IMC"] = paciente["Peso"]/(paciente["Altura"]*2)
    hospital.append(paciente)
    print()
print("==========================================")
for paciente in hospital:
    for c in paciente:
        print(c+":",paciente[c])
    print()