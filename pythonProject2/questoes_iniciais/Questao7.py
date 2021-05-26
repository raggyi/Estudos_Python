#QUESTÃO 07 - Faça um algoritmo por meio de fluxograma para ler duas variáveis inteiras A e B e garantir que A e
# B fiquem em ordem crescente, ou seja, a variável A deverá armazenar o menor valor fornecido e a variável B o maior.
def variaint():
    n1=int(input('Digite um número:'))
    n2=int(input('Digite outro número:'))
    n3=n1
    if n1<n2:
      n1=n2
      print(f'{n1} sempre será maior que {n3}')
    else:
        print(f'{n1} sempre será maior que {n2}')
variaint()



