#QUESTÃO 04 - Faça um algoritmo por meio de fluxograma que pergunte ao usuário quantos números deseja somar. Em seguida, leia a q
# uantidade informada de números e apresente o valor da soma, quantos números são maiores que 7 e quantos números são maiores que 9.
def soma97():
    q=int(input('Digite a quantidade de números:'))
    n=[]
    m7=0
    m9=0
    soma=0
    for i in range(q):
        pergunta = int(input('Digite um número:'))
        n.append(pergunta)
        soma = soma + pergunta
        if pergunta > 7:
            m7 = m7 + 1

        if pergunta > 9:
            m9= m9+1
    print(f'Números digitados: {n}')
    print(f'Soma:{soma}')
    print(f'Maiores que 7: {m7}')
    print(f'Maiores que 9: {m9}')
soma97()
