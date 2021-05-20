import random

def RecebeJogadores(quant):
	jogadores = [""]
	for l in range (1, quant + 1):
		print("Qual o apelido do {}° jogador:".format(l))
		jogadores.append(input()[0:2].upper())
	return jogadores

def IniciaTab(casas, quant, jogadores):
	tabuleiro = [[]]
	for c in range (casas):
		tabuleiro[0].append(str(c).zfill(2))
	for l in range(1, quant+1):
		raia = []
		raia.append(jogadores[l])
		for c in range(1,casas):
			raia.append("  ")
		tabuleiro.append(raia)
	return tabuleiro

def MontaTab(quant, tabuleiro, jogadores):
	print(jogadores[1: quant+1])
	print("_"*52)
	for raia in tabuleiro:
		linha = ""
		for col in raia:
			linha += '|' + col
		linha += '|'
		print(linha)
		print('-'*52)

def LancaDado(j,jogadores):
	print(jogadores[j], "tecle enter para lançar o dado. (1..6):")
	input()
	resultado = random.randrange(1,7)
	print("rolando dado...")
	print(jogadores[j], "Resultados:", resultado)
	return resultado

def MoverJogador(j,inc,jogadores,tabuleiro,fim):
	inicio = pa (j,jogadores,tabuleiro)
	destino = inicio+ inc
	if destino >= fim:
		destino = fim
	tabuleiro[j][destino] = jogadores[j]
	tabuleiro[j][inicio] = "  "
	return tabuleiro

def pa (l,jogadores,tabuleiro):
	return tabuleiro[l].index(jogadores[l])

def VerificaVencedor(quant,jogadores,tabuleiro,fim):
	vencedor = ""
	for j in range(1, quant+1):
		if pa(j,jogadores,tabuleiro) == fim:
			vencedor = jogadores[j]
			arquivoVencedor = open("Vencedor.txt","w")
			arquivoVencedor.write("Parabéns {}, você venceu jogo.".format(vencedor))
		return vencedor

def Finaliza(quant,jogadores,vencedor,tabuleiro,fim):
	for j in range (1, quant+1):
		if jogadores[j] != vencedor:
			dec = pa(j,jogadores,tabuleiro) * -1
			MoverJogador(j,dec,jogadores,tabuleiro,fim)
		print("Parabéns {}, você venceu o jogo.".format(vencedor))
		MontaTab(quant, tabuleiro, jogadores)

def VerificaPrenda(j,quant,jogadores,tabuleiro,fim):
	PosicoesPrenda = [4,9,15]
	if pa(j,jogadores,tabuleiro) in PosicoesPrenda:
		if pa(j,jogadores,tabuleiro) == 4:
			print(jogadores[j]+" PRENDA: volte 2 casas!")
			MoverJogador(j,-2,jogadores,tabuleiro,fim)
		elif pa(j,jogadores,tabuleiro) == 9:
			msg = "PRENDA: escolha um jogador para avançar 2 casas:"
			je = IdentificaEscolhido(j,msg,jogadores)
			MoverJogador(je,2,jogadores,tabuleiro,fim)
			print(jogadores[j]+" PRENDA:jogador "+jogadores[je]+" Avançou 2 casas.")
		elif pa(j,jogadores,tabuleiro) == 15:
			print(jogadores[j]+" PRENDA: volte para o inicio do jogo!")
			dec = pa(j,jogadores,tabuleiro) * -1
			MoverJogador(j,dec,jogadores,tabuleiro,fim)
		MontaTab(quant, tabuleiro, jogadores)

def VerificaBonus(j,quant,jogadores,tabuleiro,fim):
	PosicoesBonus = [6,11,13]
	if pa(j,jogadores,tabuleiro) in PosicoesBonus:
		if pa(j,jogadores,tabuleiro) == 6:
			print(jogadores[j]+" BÔNUS: avance para a casa 10!")
			MoverJogador(j,4,jogadores,tabuleiro,fim)
		elif pa(j,jogadores,tabuleiro) == 11:
			print(jogadores[j]+" BÔNUS: avance 1 casa!")
			MoverJogador(j,1,jogadores,tabuleiro,fim)
		elif pa(j,jogadores,tabuleiro) == 13:
			msg =" BÔNUS: escolha um jogador para voltar 2 casas:"
			je = IdentificaEscolhido(j,msg,jogadores)
			MoverJogador(je,-2,jogadores,tabuleiro,fim)
			print(jogadores[j]+" BÔNUS:jogador "+jogadores[je]+" voltou 2 casas.")
		MontaTab(quant, tabuleiro, jogadores)

def IdentificaEscolhido(j,msg,jogadores):
	JogadoresElegiveis = jogadores.copy()
	JogadoresElegiveis.pop(j)
	JogadoresElegiveis.pop(0)
	nje = " "
	while nje not in JogadoresElegiveis:
		if nje not in JogadoresElegiveis and nje != "":
			print("Jogador inválido: informe o nome de um jogador da lista:")
		print(jogadores[j]+msg)
		print(JogadoresElegiveis)
		nje = input().upper()
	return jogadores.index(nje) 