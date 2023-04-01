# Abrir o arquivo notas.txt


with open('notas.txt', 'r') as file:
    # Ler todas as linhas do arquivo
    linhas = file.readlines()

# Criar três listas vazias para armazenar os alunos aprovados, em exame e reprovados
aprovados = []
exame = []
reprovados = []

# Iterar por cada linha do arquivo de notas
for linha in linhas:
    # Dividir a linha em partes separadas por vírgula
    partes = linha.split(',')
    # A primeira parte é o nome do aluno
    nome = partes[0]
    # As outras partes são as notas, que serão convertidas para float
    notas = [float(nota) for nota in partes[1:]]
    # Calcular a média das notas
    media = sum(notas) / 3
    # Verificar o resultado do aluno e adicionar à lista correspondente
    if media >= 7:
        aprovados.append((nome, media))
    elif 6.9 > media >= 5:
        exame.append((nome, media))
    else:
        reprovados.append((nome, media))

# Salvar as informações nos arquivos correspondentes
with open('aprovados.txt', 'w') as file:
    for aluno in aprovados:
        file.write(f'{aluno}: {aluno}\n')

with open('exame.txt', 'w') as file:
    for aluno in exame:
        file.write(f'{aluno}: {aluno}\n')

with open('reprovados.txt', 'w') as file:
    for aluno in reprovados:
        file.write(f'{aluno}: {aluno}\n')
print('Alunos aprovados: {}\n Alunos reprovados: {}\n Alunos em exame: {}'.format(aprovados, reprovados, exame))
