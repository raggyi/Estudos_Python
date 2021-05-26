#QUESTÃO 06 - Faça um algoritmo por meio de fluxograma para ler dois números inteiros e informar se estes números
# são iguais ou diferentes.
def numint():
    n1=int(input('Digite o primeiro número:'))
    n2=int(input('Digite o segundo número:'))
    if n1==n2:
        print('Você colocou números iguais!')
    else:
        print('Parabéns você colocou dois número diferentes.')
numint()