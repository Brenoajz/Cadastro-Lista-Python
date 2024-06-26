import json
import os

def carregar_produtos():
    return json.load(open('produtos.json', 'r')) if os.path.exists('produtos.json') else []

def salvar_produtos(produtos):
    with open('produtos.json', 'w') as arquivo:
        json.dump(produtos, arquivo, indent=4)

def cadastrar_produto():
    try:
        nome = input("Nome do produto: ").strip()
        descricao = input("Descrição do produto: ").strip()
        valor = float(input("Valor do produto: "))
        disponivel = input("Disponível para venda (1 - sim / 2 - não): ").strip() == '1'
        
        if not all([nome, descricao, valor]):
            raise ValueError("Todos os campos devem ser preenchidos corretamente.")
        
        produtos = carregar_produtos()
        produtos.append({"nome": nome, "descricao": descricao, "valor": valor, "disponivel": disponivel})
        salvar_produtos(produtos)
        
        print("Produto cadastrado com sucesso!")
        listar_produtos()
    
    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def listar_produtos():
    try:
        produtos = sorted(carregar_produtos(), key=lambda x: x['valor'])
        print("\nLista de Produtos:\nNome                 Valor     \n" + "-" * 30)
        for produto in produtos:
            print(f"{produto['nome']:<20} R${produto['valor']:<10.2f}")
        
        resposta = input("\nDeseja cadastrar um novo produto? (1 - sim / 2 - não): ")
        
        if resposta == '1':
            cadastrar_produto()
        elif resposta == '2':
            print("Programa encerrado.")
        else:
            print("Opção inválida...")
            listar_produtos()
    
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def main():
    print("Bem-vindo ao sistema de cadastro de produtos!")
    listar_produtos()

if __name__ == "__main__":
    main()
