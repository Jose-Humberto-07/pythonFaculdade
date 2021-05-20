'''
Construa um algoritmo em Python que receba um valor em reais e converta para a moeda 
escolhida pelo usuário. As moedas possíveis devem ser dólar, euro e libra (valor em reais / 
taxa de cambio).
Ex. Valor em Reais: 2750,00; Taxa de Cambio: 5,50
2750/5.5 = 500.00
'''

#VARIAVEIS
EU = 6.69
LB = 7.88
DL = 5.66

print ("========= CONVERSOR DE MOEDAS =========")
print ("Qual valor você deseja converter ?")
RL = float(input ())
print ("Para qual moeda deseja converter ? Dolar (1), Euro(2), Libra (3)")
moeda = input ()

if moeda == '1': 
  print ("O valor em Dolares é:", RL/DL)
elif moeda == '2':
  print ("O valor em Euro é:", RL/EU)
else:
  print ("O valor em Libras é:", RL/LB)




