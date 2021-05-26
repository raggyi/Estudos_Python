#QUESTÃO 13 - Elabore um algoritmo por meio de fluxograma que leia um número indeterminado de idades, dos indivíduos de
# ma determinada cidade, calcule e imprima a idade média deste grupo de indivíduos. Adote a ida
# de de valor “0” (zero) como condição de finalização da leitura.
def medidades(idades):
    n=len(idades)
    x=n
    soma=0

    for i in range(n):
        soma=soma+idades[i]
        if idades[i]==0:
            print(soma/i)
            break
        else:
            if i+1 == n:
                print(soma/n)

medidades([10,11,12,11,13,0,5,4,5])

