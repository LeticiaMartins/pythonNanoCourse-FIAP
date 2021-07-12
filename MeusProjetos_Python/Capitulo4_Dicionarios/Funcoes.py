def perguntar():
    resposta = input("O que deseja realizar?"
              + "<I> - Para Inserir um usuário"
              + "<P> - Para Pesquisar um usuário"
              + "<E> - Para Excluir um usuário"
              + "<L> - Para Listar um usuário: ").upper()
    return resposta

def inserir(dicionario):
    chave = input("Digite o login: ").upper()
    dicionario[chave] = [input("Digite o nome: ").upper(),
                       input("Digite a última data de acesso: "),
                       input("Qual a última estação acessada: ").upper()]

def pesquisar(chave, dicionario):
    lista = dicionario.get(chave)
    if lista != None:
        print("Nome............: " + lista[0])
        print("Último acesso ..: " + lista[1])
        print("Última estação..: " + lista[2])

def excluir(chave, dicionario):
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print("Objeto deletado")


def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto......")
        print("Login: ", chave)
        print("Dados: ", valor)