##Crie uma lista vazia que armazene números inteiros. Em seguida, crie uma função
# que adicione um número inteiro no início da lista e outra que adicione um número
# inteiro no final da lista.
numeros = []
for i in range(5):
    ns = int(input('Digite um números inteiros '))
    numeros.append(ns)
print(numeros)
n_lista = [numeros]
n_lista.insert(0,8)
n_lista.append(10)
print(n_lista)