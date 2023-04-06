#Desenvolva um algoritmo que solicite ao usuário um número inteiro e verifique se o
# número digitado é par. Se o número for ímpar, levante uma exceção personalizada com
# uma mensagem de erro apropriada. Em seguida, imprima uma mensagem informand que o número digitado é par.
num = int(input('Digite um número: '))

try:
    if num % 2 == 1:
        raise Exception('O número é ímpar')
except Exception as e:
    print(e)

else:
    print('O número é par')