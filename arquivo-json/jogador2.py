import json

with open('C:/Users/humbe/OneDrive/Documentos/Faculdade/3°-Semestre/estrutura-de-dados/pythonnocurso/meuscodigos/arquivo-json') as f:
    jogador=json.load(f)


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