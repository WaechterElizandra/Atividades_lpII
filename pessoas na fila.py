#Crie uma fila que armazene as pessoas que estão esperando em uma fila.
# Em seguida, crie uma função que remova a primeira pessoa da fila.
from collections import deque

pessoas = deque()

pessoas.append('ELIZANDRA')
pessoas.append('EGON')
pessoas.append('IASMYN')
pessoas.append('IAGO')

print("elmentos iniciais")
print(pessoas)

print("\nElementos retirados da fila")
print(pessoas.popleft())


print("\nFila após retirar elementos")
print(pessoas)

