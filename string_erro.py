#Desenvolva um algoritmo que solicite ao usuário que digite uma string e verifique se a
# string contém apenas letras maiúsculas. Se a string contiver letras minúsculas, levante
# uma exceção embutida com uma mensagem de erro apropriada. Em seguida, imprima
# uma mensagem informando que a string contém apenas letras maiúsculas.
try:
    tx = str(input('digite uma letra: '))
    if tx != tx.upper():
        raise Exception('Letra minúscula')
except Exception as e:
    print(e)

else:
    print('Letra maiuscula')



