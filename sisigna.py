#Sistema Simples De Gestão De Notas De Alunos - Sisigna :)
#1ª parte:
# Cadastro de Notas:
# • O sistema deve permitir que o usuário insira as notas dos alunos.
# • As notas devem ser armazenadas em uma lista.

lista_de_notas = [] #lista para armazenar as notas
print("Bem vindo ao Sisigna - Sistema Simples de Gestão de Notas de Alunos") #mensagem de boas vindas e confirmação de inicialização da lista

quantidade_notas = int(input("Quantas notas você deseja inserir? ")) #solicita a quantidade de notas que o usuário quer inserir
for i in range(quantidade_notas): #loop para inserir as notas na quantidade desejada
    nota_inserida = float(input(f"Insira a nota {i+1}: ")) #solicita a nota
    lista_de_notas.append(nota_inserida) #adiciona a nota na lista a cada iteração
    print(f"Nota {i+1} inserida!") #confirmação de inserção de nota para o usuário

#2ª parte:
# Cálculo da Média:
# • O sistema deve calcular a média das notas inseridas.

media_das_notas_inseridas = sum(lista_de_notas)/len(lista_de_notas) #cálculo da média das notas inseridas
print(f"A média das notas inseridas é: {media_das_notas_inseridas:.2f}") #exibe a média das notas inseridas (2 casas decimais)

#3ª parte:
# Determinação da Situação:
# • Se a média for maior ou igual a 7, o aluno está aprovado.
# • Se a média for menor que 7, o aluno está reprovado.

situação_do_aluno = "Notas Pendentes" #inicializa a variável de situação do aluno como notas pendentes até a verificação
if media_das_notas_inseridas >= 7: #verifica se a média é maior ou igual a 7
    situação_do_aluno = "Aprovado" #se for maior ou igual a 7, o aluno está aprovado
else: #se não for maior ou igual a 7, ou seja, se for menor que 7:
    situação_do_aluno = "Reprovado" #o aluno está reprovado
print(f"A situação do aluno é: {situação_do_aluno}") #exibe a situação do aluno

#4ª parte:
# Relatório Final:
# • Exibir as notas inseridas, a média e a situação do aluno

print("\nCarregando relatório final\n") #mensagem para iniciar o relatório final
print("1 - Notas inseridas: ") #mensagem para anunciar as notas inseridas
for i, nota in enumerate(lista_de_notas): #loop para exibir cada nota inserida
    print(f"Nota {i+1}: {nota}") #exibe cada nota com a ordem que foi inserida

print(f"2 - A média das notas inseridas é: {media_das_notas_inseridas:.2f}") #exibe a média das notas inseridas (2 casas decimais)
print(f"3 - A situação do aluno é: {situação_do_aluno}\n") #exibe a situação do aluno
print("Relatório final concluído. Obrigado por usar o Sisigna!") #mensagem de conclusão do relatório final