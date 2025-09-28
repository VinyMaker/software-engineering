print("\n---------------------------- Conexão com banco SQLite, criação da tabela e inserção de dados (passo 1) ----------------------------")
# Passo 1 e 1.1: Conexão com banco SQLite, criação da tabela e inserção de dados
import sqlite3  # Biblioteca para manipular bancos SQLite
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Conectar/criar o banco de dados SQLite
conexao = sqlite3.connect('dadosvendas.db')  # Arquivo local de banco SQLite
cursor = conexao.cursor()

# Criar a tabela 'vendas1' caso não exista, com os campos necessários
cursor.execute(''' CREATE TABLE IF NOT EXISTS vendas1 (
    idvenda INTEGER PRIMARY KEY AUTOINCREMENT,
    datavenda DATE,
    produto TEXT,
    categoria TEXT,
    valorvenda REAL);''')

# Inserir registros exemplares na tabela vendas1
cursor.execute('''INSERT INTO vendas1 (datavenda, produto, categoria, valorvenda) VALUES
('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
('2023-01-05', 'Produto B', 'Roupas', 350.00),
('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
('2023-03-15', 'Produto D', 'Livros', 200.00),
('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
('2023-04-02', 'Produto F', 'Roupas', 400.00),
('2023-05-05', 'Produto G', 'Livros', 150.00),
('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
('2023-07-20', 'Produto I', 'Roupas', 600.00),
('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
('2023-09-30', 'Produto K', 'Livros', 300.00),
('2023-10-05', 'Produto L', 'Roupas', 450.00),
('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
('2023-12-20', 'Produto N', 'Livros', 250.00);''')

# Confirmar as alterações e fechar cursor/conexão/ponteiro
conexao.commit()
cursor.close()
print("Tabela vendas1 criada e dados inseridos com sucesso.")

print("\n---------------------------- Carregar e explorar os dados usando Pandas (passo 2) ----------------------------")
# Passo 2: Carregar e explorar os dados usando Pandas
df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conexao)

print("----> Visualizando as primeiras linhas dos dados:")
print(df_vendas.head())

print("----> Informações sobre as colunas e tipos de dados:")
print(df_vendas.info())

print("----> Estatísticas descritivas das colunas numéricas:")
print(df_vendas.describe())

#Fechar a conexão (após carregar os dados no DataFrame, já que não será mais usada)
conexao.close()

print("\n---------------------------- Análise dos dados (passo 3) ----------------------------")
# Passo 3: Análise dos dados
total_vendas = len(df_vendas)
print(f"----> Total de registros de vendas: {total_vendas}")

print("----> Verificação de valores nulos e dados faltantes:")
print(df_vendas.isnull().sum())

# Agrupar vendas por categoria
vendas_por_categoria = df_vendas.groupby('categoria').size().reset_index(name='quantidade_vendas')
print("----> Quantidade de vendas por categoria:")
print(vendas_por_categoria)

# Calcular faturamento total por categoria
faturamento_por_categoria = df_vendas.groupby('categoria')['valorvenda'].sum().reset_index()
print("----> Faturamento total por categoria:")
print(faturamento_por_categoria)

# Calcular valor médio por venda em cada categoria
media_vendas_categoria = df_vendas.groupby('categoria')['valorvenda'].mean().reset_index()
print("----> Valor médio por venda por categoria:")
print(media_vendas_categoria)

print("\n---------------------------- Visualização dos dados com gráficos (passo 4) ----------------------------")
# Passo 4: Visualização dos dados com gráficos
plt.figure(figsize=(10,6))
sns.barplot(x='categoria', y='quantidade_vendas', data=vendas_por_categoria, palette='viridis')
plt.title('---> Quantidade de Vendas por Categoria <---')
plt.xlabel('Categoria')
plt.ylabel('Quantidade de Vendas')
plt.show()

plt.figure(figsize=(10,6))
sns.barplot(x='categoria', y='valorvenda', data=faturamento_por_categoria, palette='magma')
plt.title('---> Faturamento Total por Categoria <---')
plt.xlabel('Categoria')
plt.ylabel('Faturamento')
plt.show()

plt.figure(figsize=(10,6))
sns.boxplot(x='categoria', y='valorvenda', data=df_vendas, palette='Set2')
plt.title('---> Distribuição dos Valores de Venda por Categoria <---')
plt.xlabel('Categoria')
plt.ylabel('Valor da Venda')
plt.show()

print("\n---------------------------- Análise e sugestões baseadas nos dados visualizados (passo 5) ----------------------------")
# Passo 5: Análise e sugestões baseadas nos dados visualizados
print("""Análise e Sugestões:
- A categoria Eletrônicos gera o maior faturamento, com valores de venda variados, indicando diversidade e necessidade de monitoramento.
- Roupas e Livros possuem volumes relevantes, com roupas mostrando menor variação nos preços.
- Distribuições indicam diferentes nichos dentro da empresa.
- Dados sem valores faltantes confirmam a confiança na análise.
Para melhorias, recomenda-se:
- Análise temporal para identificar sazonalidade.
- Inclusão de dados sobre localidades, canais de venda e avaliação de clientes.
- Sistema automatizado para monitoramento dos indicadores.
- Ações de marketing direcionadas conforme receita e demanda.""")