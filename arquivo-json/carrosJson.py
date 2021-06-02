import json
'''
teste = {
    "nome": "",
    "idade": 0,
    "altura": 0.0,
    "peso": 0.0,
    "sexo": ""
}


carros_json='{"marca":"honda,"modelo":"HRV""cor":"prata"}'

carros=json.loads(carros_json)

print(carros["marca"])

print(carros)

for i in carros:
    print()
    
for i in carros.values():
    print(i)

for i in carros.items():
    print(i)

'''


#convertndo dicionário em arquico json....
carros = {
    "marca":"honda",
    "modelo":"HRV",
    "cor":"prata"
}

carros_json = json.dumps(carros)

print(carros_json)



