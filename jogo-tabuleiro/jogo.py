import funcoes as f

casas = 17
fim = casas - 1
vencedor = ""
print(("+"*23)+" O JOGO "+("+"*23))
print("Quanto jogadores vão jogar? ")
quant = int(input())
if quant > 4 : quant = 4;
jogadores = f.RecebeJogadores(quant)
tabuleiro = f.IniciaTab(casas, quant, jogadores)
print(("+"*23)+" Inicio "+("+"*23))
f.MontaTab(quant,tabuleiro,jogadores)
rod = 1
while vencedor == "":
	print(('+'*21)+"{}° RODADA ".format(rod)+('+'*21))
	for j in range(1, quant+1):
		if vencedor == "":
			r = f.LancaDado(j,jogadores)
			tabuleiro = f.MoverJogador(j,r,jogadores,tabuleiro,fim)
			f.MontaTab(quant, tabuleiro, jogadores)
			f.VerificaPrenda(j,quant,jogadores,tabuleiro,fim)
			f.VerificaBonus(j,quant,jogadores,tabuleiro,fim)
			vencedor = f.VerificaVencedor(quant,jogadores,tabuleiro,fim)
	rod += 1
	print()
f.Finaliza(quant,jogadores,vencedor,tabuleiro,fim)


