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
