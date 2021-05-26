#QUESTÃO 14 - Elabore um algoritmo por meio de fluxograma que leia um conjunto de números e imprima o M
# AIOR, o MENOR, a SOMA e o PRODUTO deles.
def q14():
    n=int(input('Digite a quantidade de números que deseja utilizar:'))
    soma=0
    mult=1
    lista=[]
    for i in range (n):
        n1=int(input('Digite um número:'))
        lista.append(n1)
        soma=soma+n1
        mult=mult*n1
    print(soma)
    print(mult)
    print(max(lista))
    print(min(lista))
q14()


