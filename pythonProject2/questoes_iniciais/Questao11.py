#QUESTÃO 11 - Elabore um algoritmo por meio de fluxograma que imprima os núm
# eros entre 0 e 20, em ordem descendente.
def num():
    numeros=[i for i in range(21)]
    print(f'{numeros[::-1]}')
num()

