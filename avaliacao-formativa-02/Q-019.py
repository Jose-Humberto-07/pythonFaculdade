paciente = {"nome":"","idade":"","peso":0.0,"altura":0.0}
for c in paciente:
    print("Qual o(a)",c,"do paciente?")
    if c in ["altura","peso"]:
       paciente[c] = float(input())
    else:
        paciente[c] = input()        
paciente["IMC"] = (paciente["peso"]/(paciente["altura"]*2))
 
print("==========================================")
for c in paciente:
    print(c+":",paciente[c])