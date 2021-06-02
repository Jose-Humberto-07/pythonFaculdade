import json

#dictionary -> objeto json
carrosDicionario = {
    "marca": "toyota",
    "modelo": "corola",
    "cor": "preto"
}

#list -> array json
carrosList = ["honda", "volkswagem", "ford", "fiat", "chevrolet"]

#tupla -> array json
carrosTupla = ("honda", "volkswagem", "ford", "fiat", "chevrolet")


carros_D=json.dumps(carrosDicionario, indent=4, separators=(":","="), sort_keys=True)
print(carros_D)
print()

carros_L=json.dumps(carrosList)
print(carros_L)
print()

carros_T=json.dumps(carrosTupla)
print(carros_T)
print()
