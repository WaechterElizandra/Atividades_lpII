alunos = []
avaliacao = []
for i in range(3):
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)
    nota1 = float(input("Digite a primeira nota: "))
    avaliacao.append(nota1)
    nota2 = float(input("Digite a segunda nota: "))
    avaliacao.append(nota2)
    nota3 = float(input("Digite a terceira nota: "))
    avaliacao.append(nota3)


    with open("notas.txt", "w") as arquivo: #with é utilizado para abrir o arquivo e garantir que ele será fechado ao final da operação.
        arquivo.write(f"Nome: {alunos}\n")
        arquivo.write(f"Nota 1: {avaliacao}\n")
        arquivo.write(f"Nota 2: {avaliacao}\n")
        arquivo.write(f"Nota 3: {avaliacao}\n")
    #O modo "w" utilizado na função open() indica que o arquivo será aberto em modo de escrita (write),
    # o que permite escrever as informações nele.
    # As informações utilizando a função write() incluem as variáveis em formato de string