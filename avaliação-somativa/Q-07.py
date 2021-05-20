jogos = [["     ","ceará","bahia","sport","river"]]
for c in range(1,5):
    resultados = [jogos[0][c]]
    for adv in range(1,5):
        if resultados[0] != jogos[0][adv]:
            gol_aft = str(c+adv+1)
            gol_adv = str(adv)
            result = gol_aft+" x "+gol_adv
        else:
            result = "*****"
        resultados.append(result)
    jogos.append(resultados)
for resultados in jogos:
    print(resultados)