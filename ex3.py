codigo = input("Digite o código do produto: ")
nome = input("Digite o nome: ")
quantidade = input("Digite a quantidade: ")
preco = input("Digite o preço: ")

print("Código do produto: " + codigo + "\n")

print("Nome do produto: " + nome + "\n")

print("A quantidade: " + quantidade + "\n")

print("Valor da unidade: " + preco + "\n")

print("Total da compra: " + str(int(quantidade) * float(preco)))