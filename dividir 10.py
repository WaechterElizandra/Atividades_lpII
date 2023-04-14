#Desenvolva um algoritmo que solicite ao usuário que digite um número inteiro e divida 10 pelo número digitado.
# Se o número digitado for 0, levante uma exceção embutida com uma mensagem de erro apropriada. Em seguida, imprima o resultado da divisão.
n = int(input('Digite um número: '))

try:
    c = 10 / n

except ZeroDivisionError:
    print('Não é possível fazer uma divisão por zero!')
print('10 divido pelo número {} é igual a {}'.format(n,c))