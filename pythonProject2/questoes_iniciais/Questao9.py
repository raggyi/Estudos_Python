#QUESTÃO 09 - Faça um algoritmo por meio de fluxograma para imprimir os números pares existentes entre 1 até 50.
def pares():
    for i in range(51):
        if (i+1) % 2 == 0:
         print(i+1)
pares()

