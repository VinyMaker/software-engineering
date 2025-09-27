#Sistema Simples De Gestão De Livros - Sisili ;)
#1ª parte:
# Definir a Classe Livro:

import matplotlib.pyplot as plt #aqui, de praxe, importamos antecipadamente a biblioteca para criar gráficos

class Livro: #cria a classe Livro
    def __init__(self, titulo, autor, genero, quantidade): #construtor da classe com atributos do livro):
        #abaixo os atributos do livro
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

#2ª parte:
# Definir a Biblioteca de Livros e Inicialização do Sisili:
biblioteca = [] #lista usada para armezenar os livros
print(f"Bem vindo ao Sisili - Sistema Simples de Gestão de Livros") #mensagem de boas vindas e confirmação de que o sistema inicou corretamente

#3ª parte:
# Definição das Funções disponíveis no Sisili:
def cadastrar_livro(biblioteca, titulo, autor, genero, quantidade): #função para cadastrar um livro na biblioteca
    print(f"\nCadastrando livro na biblioteca...")
    novo_livro = Livro(titulo, autor, genero, quantidade)
    biblioteca.append(novo_livro) #adiciona o livro na biblioteca
    print(f"Livro '{titulo}' cadastrado com sucesso!") #confirmação de cadastro do livro

def listar_livros(biblioteca): #função para listar os livros da biblioteca
    print(f"\nListando livros da biblioteca...")
    if not biblioteca: #usado para verificar se a biblioteca está vazia
        print("A biblioteca está vazia.")
    else:
        for cada_livro in biblioteca:
            print(f"Título: {cada_livro.titulo}, Autor: {cada_livro.autor}, Gênero: {cada_livro.genero}, Qtde: {cada_livro.quantidade}")

def buscar_livro_por_titulo(biblioteca, titulo_procurado): #função para buscar um livro pelo título, que precisa de uma biblioteca e o título do livro
    print(f"\nBuscando por '{titulo_procurado}' na biblioteca...")
    encontrado = False #cria um marcador para indicar se achou ou não algum resultado
    for cada_livro in biblioteca:
        if cada_livro.titulo.lower() == titulo_procurado.lower(): #verifica o título, ignorando maiúsculas e minúsculas
            print(f"Título Encontrado: {cada_livro.titulo}, Autor: {cada_livro.autor}, Gênero: {cada_livro.genero}, Quantidade: {cada_livro.quantidade}")
            encontrado = True #marca como encontrado
    if not encontrado: #só mostrará se nenhum resultado foi localizado
        print(f"Nenhum resultado para '{titulo_procurado}' encontrado na biblioteca.")

#4ª parte:
# Definição e Formulação do Gráfico de Gêneros dos Livros
def gerar_grafico_por_genero(biblioteca): #função para gerar um gráfico por gênero de livros da biblioteca
    print(f"\nGerando gráfico por gênero da biblioteca...")
    contagem_de_generos = {} #inicializa o dicionário para contar os gêneros da biblioteca
    for cada_livro in biblioteca:
        if cada_livro.genero in contagem_de_generos:
            contagem_de_generos[cada_livro.genero] += cada_livro.quantidade #adiciona o gênero se já existir no contador
        else:
            contagem_de_generos[cada_livro.genero] = cada_livro.quantidade #adiciona o gênero se não existir no contador
    
    #Formulação do gráfico
    generos = list(contagem_de_generos.keys()) #lista de gêneros por chave do contador
    quantidades = list(contagem_de_generos.values()) #lista de quantidades em valores do contador

    #Criação do Gráfico
    plt.bar(generos, quantidades)
    plt.xlabel('Gênero dos Livros')
    plt.ylabel('Quantidade de Livros')
    plt.title('Livros por Gênero')
    plt.show()

# Exemplos para teste das funções:
cadastrar_livro(biblioteca, "Dom Casmurro", "Machado de Assis", "Romance", 3)
cadastrar_livro(biblioteca, "Harry Potter e a Pedra Filosofal", "J.K. Rowling", "Fantasia", 5)
cadastrar_livro(biblioteca, "Harry Potter e a Câmara Secreta", "J.K. Rowling", "Fantasia", 4)
cadastrar_livro(biblioteca, "Pai Rico, Pai Pobre", "Robert Kiyosaki", "Autoajuda", 7)
listar_livros(biblioteca)
buscar_livro_por_titulo(biblioteca, "Dom Casmurro")
gerar_grafico_por_genero(biblioteca)