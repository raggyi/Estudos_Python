#QUESTÃO 05 - Faça um algoritmo por meio de fluxograma que lê o nome de um produto, o preço e a quantidade comprada. Escrev
# a o nome do produto comprado e o valor total a ser pago, considerando que são oferecidos descontos pelo número de unidades compradas, segundo a tabela abaixo:
#a) Até 10 unidades: valor total
#b) De 11 a 20 unidades: 10% de desconto
#c) De 21 a 50 unidades: 20% de desconto
#d) Acima de 50 unidades: 25% de desconto
def preçojusto():
    produto=str(input('Digite o nome do produto:'))
    preço=float(input('Digite o preço do produto:'))
    qtd=float(input('Digite a quantidade comprada do produto:'))
    if qtd <= 10:
        preço= preço
    elif qtd <=20:
        preço= preço-(preço *(10/100))
    elif qtd <= 50:
        preço= preço-(preço * (20/100))
    elif preço > 50:
        preço=preço-(preço*(25/100))
    print(f'O produto desejado foi: {produto}')
    print(f'O preço da unidade produto desejado foi:R${preço}')
    print(f'A quantidade desejada foi de: {qtd}')
    print(f'O preço total foi: {preço*qtd}')
preçojusto()