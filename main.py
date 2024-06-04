from menu import ShowMenu

def main():
    while True:
        opcao = ShowMenu(["Adicionar", "Buscar", "Remover"], "Tabela Hash", "Sair")
        match opcao:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case _:
                break


# Exemplo de switch case em Python
# match term:
#     case pattern-1:
#             action-1
#     case pattern-2:
#             action-2
#     case pattern-3:
#             action-3
#     case _:
#         action-default


if __name__ == '__main__':
    main()

# Requisitos:
# 1. Implemente uma classe chamada TabelaHash que ser´a respons´avel por armazenar os nomes na tabela hash.
# 2. Dentro da classe TabelaHash, implemente os m´etodos necess´arios para adicionar, buscar e remover nomes na
# tabela.
# 3. Crie uma fun¸c˜ao chamada hash divisao que recebe um nome como parˆametro e retorna o ´ındice da tabela
# hash utilizando o M´etodo da Divis˜ao.
# 4. Crie uma fun¸c˜ao chamada hash dobra que recebe um nome como parˆametro e retorna o ´ındice da tabela hash
# utilizando o M´etodo da Dobra.
# 5. Crie uma fun¸c˜ao chamada hash multiplicacao que recebe um nome como parˆametro e retorna o ´ındice da
# tabela hash utilizando o M´etodo da Multiplica¸c˜ao.
# 6. Implemente as classes necess´arias para o tratamento de colis˜oes escolhido pelo usu´ario: Encadeamento Exterior, Encadeamento Interior ou Endere¸camento Aberto (Tentativa Sequencial).
# 7. No programa principal, solicite ao usu´ario qual tipo de fun¸c˜ao hash e tratamento de colis˜oes ele deseja utilizar.
# 8. Crie um loop que permite ao usu´ario adicionar, buscar e remover nomes na tabela hash at´e que ele decida sair
# do programa.
# 9. Exiba a tabela hash atualizada ap´os cada opera¸c˜ao.


class TabelaHash:
    def __init__(self, tamanho):
        self.tabela = {}
        self.tamanho = tamanho

    def adicionar(self, nome):
        pass
    
    def buscar(self, nome):
        pass
    
    def remover(self, nome):
        pass
    
    def hash_divisao(self, nome):
        pass
    
    def hash_dobra(self, nome):
        pass

    def hash_multiplicacao(self, nome):
        pass
    
    def encadeamento_exterior(self):
        pass
    
    def encadeamento_interior(self):
        pass
    

    