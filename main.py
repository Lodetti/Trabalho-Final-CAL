import time

def ler_itens(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        capacidade = int(f.readline().strip())
        n = int(f.readline().strip())
        linhas = f.readlines()

    itens = []
    for linha in linhas:
        id_, peso, valor, desc, frag = linha.strip().split(',')
        itens.append({
            'id': int(id_),
            'peso': int(peso),
            'valor': int(valor),
            'desc': desc,
            'fragilidade': int(frag)
        })
    return capacidade, itens


def eficiencia_fragilidade_beta(item, beta=20):
    return item['valor'] / (item['peso'] + beta * (1 / (item['fragilidade'] + 1))) #formula para obter uma eficiência considerando a fragilidade (peso que pode suportar)

# fragilidado tendendo a 0 -> eficiência baixa  
# fragilidade crescendo -> aumenta eficiência
# beta é um coeficiente limitante da influência da fragilidade

def carregar_mochila(itens, capacidade_max, beta=20):
    # Ordenar pela eficiência com fragilidade
    itens_ordenados = sorted(itens, key=lambda x: eficiencia_fragilidade_beta(x, beta), reverse=True)

    mochila = []
    peso_total = 0
                                    
    for item in itens_ordenados:   # Mochila é ordenada a partir do topo
        if peso_total + item['peso'] <= capacidade_max:
            peso_acima = peso_total
            if item['fragilidade'] >= peso_acima:  # Verifica se o elemento consegue suportar o peso que está em cima dele
                # print(eficiencia_fragilidade_beta(item, 20))
                mochila.append(item)
                peso_total += item['peso']

    valor_total = sum([i['valor'] for i in mochila])
    return mochila, valor_total


# Exemplo de uso
if __name__ == "__main__":
    tempo_inicial = time.time()
    capacidade, itens = ler_itens("itens.txt")
    mochila, valor = carregar_mochila(itens, capacidade, beta=20)
    print(capacidade)

    
    tempo_final = time.time()
    
    tempo = tempo_final - tempo_inicial
    print(tempo)
    
    # print(f"Valor total na mochila: {valor}")
    # print(f"Peso total: {sum(i['peso'] for i in mochila)}")
    # print("Itens escolhidos:")
    # for item in mochila:
    #     print(f"  {item['id']} - {item['desc']} (peso: {item['peso']}, valor: {item['valor']}, fragilidade: {item['fragilidade']})")

    