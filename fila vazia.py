#Crie uma fila vazia que armazene números inteiros.
# Em seguida, crie uma função que adicione um número inteiro no final da fila
# e outra que remova o primeiro número da fila.

fila = [] # fila vazia

def enqueue(num):#adiciona o n inteiro
    fila.append(num)

def dequeue():#remove e retorna o primeiro número da fila
    if not fila:
        print("A fila está vazia.")
    else:
        return fila.pop(0)

for i in range(5):
    enqueue(input('informe um número: '))

print('núemros inseridos na fila: ',fila)

print('núemros retirados da fila: ',dequeue())
print('Intens restantes na fila:',fila)
print(enqueue(input('informe um número: ')))
print('Intens na fila: ',fila)



