#Desenvolva um algoritmo que solicite ao usuário que digite duas strings e verifique se as strings têm o mesmo comprimento.
# Se as strings tiverem comprimentos diferentes, levante uma exceção personalizada com uma mensagem de erro apropriada.
# Em seguida, imprima uma mensagem informando que as strings têm o mesmo comprimento.
class MinhaEcecao(Exception):
    pass

try:
    string1 = input("Digite a primeira string: ")
    string2 = input("Digite a segunda string: ")
    if len(string1) != len(string2):
        raise MinhaEcecao("As strings têm comprimentos diferentes.")

except MinhaEcecao as e:
    print(e)
    print('As strings tem o mesmo comprimento.')