#EXERCICIO 1
produtos = {}

while True:
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    categoria = input("Categoria: ")
    produtos[nome] = {"preco": preco, "categoria": categoria}

    if input("Adicionar outro? (s/n): ").lower() != 's':
        break

print("Total de produtos:", len(produtos))

categorias = {}
for p in produtos.values():
    cat = p["categoria"]
    if cat not in categorias:
        categorias[cat] = []
    categorias[cat].append(p["preco"])

for cat in categorias:
    media = sum(categorias[cat]) / len(categorias[cat])
    print(f"Média de preço da categoria {cat}: {media:.2f}")

mais_caro = max(produtos.items(), key=lambda x: x[1]["preco"])
mais_barato = min(produtos.items(), key=lambda x: x[1]["preco"])

print("Mais caro:", mais_caro[0], "-", mais_caro[1]["preco"])
print("Mais barato:", mais_barato[0], "-", mais_barato[1]["preco"])


