#Crie uma lista que armazene os nomes dos países em ordem alfabética. Em
# seguida, crie uma função que receba um nome de país e retorne a posição dele na lista.
lista_países = []


for i in range(5):
    paises = str(input('digite o nome do pais: '))
    lista_países.append(paises)
organizadas = sorted(lista_países)
print(organizadas)

posição = input('Qual país deseja saber a posição? ')
print((organizadas.index(posição)))