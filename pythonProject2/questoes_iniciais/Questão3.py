from statistics import mean
valor_ingresso = 20
qtd_ig = 0
idades = []
nomes = []
desc_100= []
desc_25 = 0
valor = []
while True:
    nome = input('Digite o nome do cliente(-1 para parar):')
    if nome == "-1":
        break
    nomes.append(nome)
    idade= int(input('Digite a idade do cliente:'))
    idades.append(idade)
    if idade in range(0,6):
       valor_ingresso = 20 * 0.9
    elif idade in range(6,13):
        valor_ingresso=20 * 0.92
    elif idade in range(13,26):
        valor_ingresso=20 * 0.95
    elif idade > 60:
        valor_ingresso = 20
    else:
        valor_ingresso=20 * 0.85
    ig=int( input( 'Digite o número de ingressos adicionais que vocês deseja comprar:'))
    for i in range(ig):
        idade1 = int( input( 'Digite a idade do cliente:' ) )
        idades.append(idade1)
        qtd_ig += 1
    if ig >= 1:
        if ig ==1:
            valor.append(valor_ingresso * 0.75)
        elif ig ==2:
            valor.append(valor_ingresso* 0.5)
        elif ig ==3:
            valor.append(valor_ingresso *0.25)
        else:
            valor.append(valor_ingresso*0)
    if ig >= 4:
        desc_100.append(nome)
    if ig == 1:
        desc_25 +=1

print(50 * '-')
'RELAÇÃO 100% DESC'
for i in desc_100:
    print(i)

print(50 * '-')

print(f'A quantidade de ingressos adicionais foi de :{qtd_ig}')

print(50 * '-')

print(f' O percentual de pessoas com 25% de desconto foi de :{round(( desc_25 / len( nomes )*100), 2)}%')

print(50 * '-')

print(f'A média de valores pagos por clientes com combo foi de: R${round( mean( valor ), 2 )}')

print(50 * '-')

