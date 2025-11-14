import random

def gerar_itens(qntItens, pesoMala, descricoes, itens):
	for i in range(qntItens):
		id_obj = i + 1
		peso_obj = random.randint(1, 50)
		valor_obj = random.randint(1, 10)
		descricao_obj = random.choice(descricoes)
		fragilidade = random.randint(0, 500)
		itens.append(f"{id_obj},{peso_obj},{valor_obj},{descricao_obj},{fragilidade}\n")
	return itens
		
		
def main():
	descricoes = [
		"camiseta", "calca jeans", "meia", "cinto", "tenis", "sandalia", "chinelo",
		"carregador", "fone de ouvido", "power bank", "adaptador", "tablet",
		"protetor solar", "oculos de sol", "escova de dentes", "pasta de dente", "sabonete",
		"livro", "revista", "caderno", "caneta", "lapiseira", "borracha",
		"copo termico", "garrafa de agua", "lanche", "barra de cereal",
		"bone", "chapeu", "luva", "cachecol", "relógio", "pulseira",
		"kit costura", "kit primeiros socorros", "remedio",
		"perfume", "presente", "brincos", "colar", "pulseira",
        "boina", "saia", "vestido", "documento", "agenda", 
        "toalha", "creme", "bota", "chinelo"
		]
	
	quantos_itens_quer_gerar = 1000
	peso_da_mala = 500 
	itens_gerados = list()
	gerar_itens(quantos_itens_quer_gerar, peso_da_mala, descricoes, itens_gerados)
	
	with open("itens.txt", "w") as arquivo:
		arquivo.write(f"{peso_da_mala}\n")
		arquivo.write(f"{quantos_itens_quer_gerar}\n")
		
		for i in range(len(itens_gerados)):
			arquivo.write(itens_gerados[i])
			
	
if __name__ == "__main__":
	main()