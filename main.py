from menu import ShowMenu


# Requisitos:
# 1. Implemente uma classe chamada TabelaHash que sera responsavel por armazenar
# os nomes na tabela hash.
# 2. Dentro da classe TabelaHash, implemente os metodos necessarios para
# adicionar, buscar e remover nomes na tabela.
# 3. Crie uma funcao chamada hash divisao que recebe um nome como parametro e
# retorna o ındice da tabela hash utilizando o Metodo da Divisao.
# 4. Crie uma funcao chamada hash dobra que recebe um nome como parametro e
# retorna o ındice da tabela hash utilizando o Metodo da Dobra.
# 5. Crie uma funcao chamada hash multiplicacao que recebe um nome como 
# parametro e retorna o ındice da tabela hash utilizando o Metodo da 
# Multiplicacao.
# 6. Implemente as classes necessarias para o tratamento de colisoes escolhido
# pelo usuario: Encadeamento Exterior, Encadeamento Interior ou Enderecamento
# Aberto (Tentativa Sequencial).
# 7. No programa principal, solicite ao usuario qual tipo de funcao hash e
# tratamento de colisoes ele deseja utilizar.
# 8. Crie um loop que permite ao usuario adicionar, buscar e remover nomes na
# tabela hash ate que ele decida sair do programa.
# 9. Exiba a tabela hash atualizada apos cada operacao.


def main():
    global tabela_hash

    menu_funcao_hash()
    menu_tratamento_de_colisoes()

    tamanho_tabelha_hash = int(ShowMenu([], "Informe o tamanho da tabela"))
    tabela_hash = TabelaHash(tamanho_tabelha_hash)
    menu()

opcao_tratamento_de_colisoes = None
opcao_funcao_hash = None


class TabelaHash:
    def __init__(self, tamanho):
        # substitui o dicionario por uma lista, como nao da pra criar um
        # vertor vazio em python, criei uma lista de tamanho "tamanho" e
        # preenchi ela com "None" (do mesmo jeito que a professora fez)
        self.tabela = [None] * tamanho
        self.tamanho = tamanho


    def adicionar(self, nome):
        indice = self.calcula_index(nome)
        
        if self.tabela[indice] is None:
            self.tabela[indice] = nome
        else:
            match opcao_tratamento_de_colisoes:
                case 1:
                        pass
                case 2:
                        pass
                case 3:
                        pass
                        
                case _:
                    raise ValueError("Opção de tratamento de colisão inválida")


    # Se a pesquisa encontrar resultados, retorna indice em que
    # o nome está localizado
    # Se não, retorna False
    def pesquisa(self, nome):
        indice = self.calcula_index(nome)
        if self.tabela[indice] is not None:
            return indice
        else:
            return False


    def remover(self, nome):
        indice = self.calcula_index(nome)
        self.tabela[indice] = None


    def hash_divisao(self, nome):
        return sum(ord(c) for c in nome) % self.tamanho


    def hash_dobra(self, nome):
        pass


    def hash_multiplicacao(self, nome):
        pass

    def calcula_index(self, nome):
        match opcao_funcao_hash:
            case 1:
                return self.hash_divisao(nome)
            case 2:
                return self.hash_dobra(nome)
            case 3:
                return self.hash_multiplicacao(nome)
            case _:
                raise ValueError("Opção de hash inválida")



def menu_tratamento_de_colisoes():
    while True:
        global opcao_tratamento_de_colisoes
        tratamentos_de_colisoes = ["Encadeamento Exterior", "Encadeamento Interior", "Endereçamento Aberto"]
        opcao_tratamento_de_colisoes = ShowMenu(tratamentos_de_colisoes, "Escolha um tratamento de colisões")
        match opcao_tratamento_de_colisoes:
            case "1":
                # Encadeamento Exterior
                break
            case "2":
                # Encadeamento Interior
                break
            case "3":
                # Endereçamento Aberto
                break
            case _:
                pass


def menu_funcao_hash():
    while True:
        global opcao_funcao_hash
        funcaoes_hash = ["Divisão", "Dobra", "Multiplicação"]
        opcao_funcao_hash = ShowMenu(funcaoes_hash, "Escolha mua função hash")
        match opcao_funcao_hash:
            case "1":
                break
            case "2":
                # Encadeamento Interior
                break
            case "3":
                # Endereçamento Aberto
                break
            case _:
                pass


def menu():
    while True:
        opcao = ShowMenu(["Adicionar", "Buscar", "Remover"], "Tabela Hash", "Sair")
        match opcao:
            case "1":
                adicionar()
            case "2":
                buscar()
            case "3":
                remover()
            case _:
                break
        print(f"Tabela Hash: {tabela_hash.tabela}")
        input('Pressione Enter para continuar....')


def adicionar():
    nome = ShowMenu([], "Nome que deseja adicionar na tabela")
    tabela_hash.adicionar(nome)
    print(f'{nome} adicionado com sucesso!')


def buscar():
    nome = ShowMenu([], "Nome que deseja buscar na tabela")
    pesquisa = tabela_hash.pesquisa(nome)
    if pesquisa is False:
        print(f'O nome "{nome}" não foi encontrado!')
    else:
        print(f"O {nome} foi encontrado no endereço {pesquisa}")


def remover():
    nome = ShowMenu([], "Nome que deseja remover na tabela")
    pesquisa = tabela_hash.pesquisa(nome)
    if pesquisa is False:
        print(f'O nome "{nome}" fão encontrado!')
    else:
        tabela_hash.remover(nome)
        print(f"O {nome} foi removido da tabela!")


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
