"""
Construa um algoritmo em Python que responda o exame de doping de um atleta recebendo o nome e a a taxa de testosterona do mesmo, então retornado o resultado positivo se a testosterona for maior que 1400 ou negativo caso seja menor.
"""

nome = str(input("informe o nome do atleta: "))
taxa = float(input("informe a taxa de testosterona: "))

if(taxa > 1400):
    print("POSITIVO")
elif(taxa < 1400):
    print("NEGATIVO")

print("Volte sempre, obrigado.")        