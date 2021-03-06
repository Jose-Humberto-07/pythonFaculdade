import json

jogador = {
    "nome": "Neymar",
    "time": "PSG",
    "vivo": True,
    "energia": 100,
    "patrocinio": ["nike","adidas","puma"],
    "habilidades": [
        {"tipo": "transporte","habilidade":80},
        {"tipo": "ataque","habilidade":100},
        {"tipo": "reconhecimento","habilidade":100}
    ]
}

jogador_jason = json.dumps(jogador, indent=5,)

print(jogador_jason)
print()
print(jogador["nome"])
print()
print(jogador["habilidades"])
print()
print("=" * 65)
print()

#out put das chaves
for c in jogador:
    print(c)
print()
#itens
for c in jogador.items():
    print(c)
print()
#values
for c in jogador.values():
    print(c)
print()
#key and values
for k,v in jogador.items():
    print(k,v)
print()
for c in jogador["patrocinio"]:
    print(c)
print()
for c in jogador["habilidades"]:
    print(c["tipo"])
    print(c["habilidade"])
    print()
print()
for c in jogador["habilidades"]:
    print(c["tipo"] + " - " + str(c["habilidade"]))