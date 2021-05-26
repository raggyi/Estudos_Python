#QUESTÃO 02 - Faça um algoritmo por meio de fluxograma para listar todos os múltiplos positivos do
# número 7 menores ou iguais a 100.
def multp7(n):
    nf=n
    while n <=100:
        n=n+nf
        print(n)
multp7(7)