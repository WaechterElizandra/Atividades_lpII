#Crie uma pilha vazia que armazene números inteiros. Em seguida, crie uma função
# que adicione um número inteiro no topo da pilha e outra que remova o número inteiro no topo da pilha.
class Pilha:
    def __init__(self):
        self.items = []

    def esta_vazia(self):
        return self.items == []

    def adicionar(self, item):
        self.items.append(item)

    def remover(self):
        return self.items.pop()


# criando uma pilha vazia
pilha = Pilha()

# adicionando números inteiros na pilha
for i in range(10):
    pilha.adicionar(int(input('Digite um número: ')))


# removendo o número inteiro no topo da pilha
print(pilha.remover())


# adicionando outro número inteiro na pilha
print(pilha.adicionar(int(input('Digite um número: '))))
# removendo o número inteiro no topo da pilha novamente
print(pilha.remover())

