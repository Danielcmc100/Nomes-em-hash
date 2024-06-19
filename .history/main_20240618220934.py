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
        self.tabela = {}
        self.tamanho = tamanho


    def adicionar(self, nome):
        indice = self.calcula_index(nome)
        
        if indice not in self.tabela:
            self.tabela[indice] = nome
            print(f'{nome} adicionado com sucesso!')
        else:
            print(f"Colisão detectada no endereço {indice}")
            match opcao_tratamento_de_colisoes:
                case "1":
                        self.adiciona_exterior(indice, nome)
                case "2":
                        pass
                case "3":
                        pass        
                case _:
                    raise ValueError("Opção de tratamento de colisão inválida")



    def remover(self, nome):
        indice = self.calcula_index(nome)

        match opcao_tratamento_de_colisoes:
                case "1":
                        self.remove_exterior(indice, nome)
                case "2":
                        pass
                case "3":
                        pass        
                case _:
                    raise ValueError("Opção de tratamento de colisão inválida")


    def pesquisar(self, nome):
        indice = self.calcula_index(nome)
       
        if indice not in self.tabela:
            return False
        
        elif self.tabela[indice] == nome:
             return indice
        
        else:  
            match opcao_tratamento_de_colisoes:
                    case "1":
                            return self.pesquisa_exterior(indice, nome)
                    case "2":
                            pass
                    case "3":
                            pass        
                    case _:
                        raise ValueError("Opção de tratamento de colisão inválida")


    def adiciona_exterior(self, indice, nome):
        # Se o elemento na tabela não for uma lista, é convertido para lista
        # para que o .append() funcine
        if type(self.tabela[indice]) is not list:
            self.tabela[indice] = [self.tabela[indice]]
        
        self.tabela[indice].append(nome)


    # Essa função é chamada quando o index correspondente ao elemento pesquisado é
    # uma lista, por isso nao adicionei nenhuma verificação se é lista ou não
    def pesquisa_exterior(self, indice, nome):
        
        # Se o nome está na lista, retorna uma lista com o indice da tabela (dicionario)
        # que a lista se encontra e o indice do elemento presente na lista dentro da tabela
        if nome in self.tabela[indice]:
            return [indice, f"posição na lista: {self.tabela[indice].index(nome)}"]
        else:
            return False


    def remove_exterior(self, indice, nome):
        # Se o elemento da tabela pertencer a uma lista, ele remove apenas o elemento da lista
        if type(self.tabela[indice]) is list:
            self.tabela[indice].remove(nome)

            # Se a lista fica com tamanho 1 depois da remoção, ela é transformada num
            # elemento único (tipo string)
            if len(self.tabela[indice]) == 1:
                self.tabela[indice] = self.tabela[indice][0]

        # Caso o elemento correspondente ao indice for apenas uma string, ela é removida
        # do dicionário
        else:
            del self.tabela[indice]
        
            


    def hash_divisao(self, nome):
        return sum(ord(c) for c in nome) % self.tamanho


    def hash_dobra(self, nome):
        chave = sum(ord(c) for c in nome)
        chave_str = str(chave)
        soma_dobra = 0

        for i in range(0, len(chave_str), 2):
            soma_dobra += int(chave_str[i:i+2])

        indice = soma_dobra % self.tamanho
        return indice


    def hash_multiplicacao(self, nome):
        A = (5 ** 0.5 - 1) / 2
        chave = sum(ord(c) for c in nome)
        indice = int(self.tamanho * ((chave * A) % 1))
        return indice


    def calcula_index(self, nome):
        match opcao_funcao_hash:
            case "1":
                return self.hash_divisao(nome)
            case "2":
                return self.hash_dobra(nome)
            case "3":
                return self.hash_multiplicacao(nome)
            case _:
                raise ValueError("Opção de hash inválida")


def menu_tratamento_de_colisoes():
    while True:
        global opcao_tratamento_de_colisoes
        tratamentos_de_colisoes = ["Encadeamento Exterior", "Encadeamento Interior", "Endereçamento Aberto"]
        opcao_tratamento_de_colisoes = ShowMenu(tratamentos_de_colisoes, "Escolha um tratamento de colisões")
        opcao_tratamento_de_colisoes = "1"
        match opcao_tratamento_de_colisoes:
            case "1":
                # Encadeamento Exterior
                # Lista comun pra cada elemento
                break
            case "2":
                # Encadeamento Interior
                # Armazena as colisões na própria tabela
                # Se a posição calculada já estiver ocupada por outra chave (ocorreu uma colisão), 
                # um método de sondagem é usado para encontrar uma nova posição. Os métodos de sondagem 
                # incluem sondagem linear, sondagem quadrática e hashing duplo.
                # A chave é inserida na primeira posição vazia encontrada.
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
                print("Opção inválida")
                input("Pressione Enter para continuar...")


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
    


def buscar():
    nome = ShowMenu([], "Nome que deseja buscar na tabela")
    pesquisa = tabela_hash.pesquisar(nome)
    if pesquisa is False:
        print(f'O nome "{nome}" não foi encontrado!')
    else:
        print(f"O {nome} foi encontrado no endereço {pesquisa}")


def remover():
    nome = ShowMenu([], "Nome que deseja remover na tabela")
    pesquisa = tabela_hash.pesquisar(nome)
    if pesquisa is False:
        print(f'O nome "{nome}" fão encontrado!')
    else:
        tabela_hash.remover(nome)
        print(f"O nome {nome} foi removido da tabela!")


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
