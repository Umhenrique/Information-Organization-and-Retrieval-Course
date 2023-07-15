import pickle

# Constantes
TAMANHO_DISCO = 2048
TAMANHO_BLOCO = 8

# Class para definir a estrutura de dados
class Arquivo:
    def __init__(self, nome, tamanho, bloco_inicial):
        self.nome = nome
        self.tamanho = tamanho
        self.bloco_inicial = bloco_inicial

# Salvar a bomba quando ela fechar
def salvar_sistema_arquivos(arquivos, conteudo_disco):
    with open('sistema_arquivos.pickle', 'wb') as f:
        pickle.dump((arquivos, conteudo_disco), f)


def carregar_sistema_arquivos():
    try:
        with open('sistema_arquivos.pickle', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return [], [''] * (TAMANHO_DISCO // TAMANHO_BLOCO)


def exibir_sistema_arquivos(arquivos):
    print("Sistema de Arquivos:")
    if len(arquivos) == 0:
        print("Vazio")
    else:
        for arquivo in arquivos:
            print(f"Nome: {arquivo.nome}\tTamanho: {arquivo.tamanho}\tBlocos: {arquivo.bloco_inicial}-{arquivo.bloco_inicial + arquivo.tamanho // TAMANHO_BLOCO - 1}")

def criar_arquivo(arquivos, conteudo_disco):
    nome = input("Digite o nome do arquivo: ")
    tamanho = int(input("Digite o tamanho do arquivo em bytes: "))

    if tamanho > TAMANHO_DISCO:
        print("Tamanho do arquivo excede o tamanho do disco.")
        return

    for arquivo in arquivos:
        if arquivo.nome == nome:
            print("Já existe um arquivo com esse nome.")
            return

    blocos_necessarios = tamanho // TAMANHO_BLOCO + (1 if tamanho % TAMANHO_BLOCO > 0 else 0)
    blocos_livres = [i for i, bloco in enumerate(conteudo_disco) if bloco == '']

    if len(blocos_livres) < blocos_necessarios:
        print("Espaço em disco insuficiente para armazenar o arquivo.")
        return

    bloco_inicial = blocos_livres[0]
    for i in range(blocos_necessarios):
        conteudo_disco[bloco_inicial + i] = nome

    arquivos.append(Arquivo(nome, tamanho, bloco_inicial))
    print("Arquivo criado com sucesso.")

def remover_arquivo(arquivos, conteudo_disco):
    nome = input("Digite o nome do arquivo a ser removido: ")

    for arquivo in arquivos:
        if arquivo.nome == nome:
            for i in range(arquivo.tamanho // TAMANHO_BLOCO):
                conteudo_disco[arquivo.bloco_inicial + i] = ''
            arquivos.remove(arquivo)
            print("Arquivo removido com sucesso.")
            return

    print("Arquivo não encontrado.")

def exibir_informacoes_arquivo(arquivos):
    nome = input("Digite o nome do arquivo: ")

    for arquivo in arquivos:
        if arquivo.nome == nome:
            print(f"Nome: {arquivo.nome}\tTamanho: {arquivo.tamanho}\tBlocos: {arquivo.bloco_inicial}-{arquivo.bloco_inicial + arquivo.tamanho // TAMANHO_BLOCO - 1}")
            return

    print("Arquivo não encontrado.")

def desfragmentar_disco(arquivos, conteudo_disco):
    arquivos_ordenados = sorted(arquivos, key=lambda x: x.bloco_inicial)

    for i, arquivo in enumerate(arquivos_ordenados):
        arquivo.bloco_inicial = i
        for j in range(arquivo.tamanho // TAMANHO_BLOCO):
            conteudo_disco[i + j] = arquivo.nome

    print("Desfragmentação concluída.")

arquivos, conteudo_disco = carregar_sistema_arquivos()


# main
print("==================Cabeçalho==================")
print("|Materia: Organização e Recuperação da Informação")
print("|Docente: SEBASTIÃO EMIDIO ALVES FILHO")
print("|Discente: MATHEUS HENRIQUE ASSUNÇAO DE MEDEIROS")
print("|VITOR ELBERT FILGUEIRA LIMA")
print("|CAIO VICTOR SILVERIO SOBRAL")
print("|GUSTAVO MEDEIROS DE OLIVEIRA")
print("|Projeto: Simulador de Gerência de Sistemas de Arquivos")
print("==================Cabeçalho==================")

#main loop
while True:
    print("================================================")
    print("|[1] Criar um arquivo")
    print("|[2] Remover um arquivo")
    print("|[3] Exibir informações de um arquivo")
    print("|[4] Desfragmentar")
    print("|[5] Exibir sistema de arquivos")
    print("|[0] Sair")
    print("================================================")

    escolha = input("Digite a opção desejada: ")

    if escolha == '1':
        criar_arquivo(arquivos, conteudo_disco)
    elif escolha == '2':
        remover_arquivo(arquivos, conteudo_disco)
    elif escolha == '3':
        exibir_informacoes_arquivo(arquivos)
    elif escolha == '4':
        desfragmentar_disco(arquivos, conteudo_disco)
    elif escolha == '5':
        exibir_sistema_arquivos(arquivos)
    elif escolha == '0':
        salvar_sistema_arquivos(arquivos, conteudo_disco)
        break
    else:
        print("Opção inválida. Tente novamente.")
