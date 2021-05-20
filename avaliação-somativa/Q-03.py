velocidade = 84
if velocidade <= 30:
    print("Baixa")
elif velocidade > 30 and velocidade <= 80:
    print("Baixa")
elif velocidade > 80 and velocidade <= 120:
    print("Alta")
elif velocidade > 120 and velocidade <= 180:
    print("Muito Alta")
else:
    print("Acima da velocidade permitida")