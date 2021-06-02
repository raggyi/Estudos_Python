from statistics import mean

valor_ingresso = 20
idades = []
nomes = []
precos = []
idosos = []
valores_desc = []
count_desc = 0
count_10 = 0

while True:
    nome = input('Digite o nome do cliente(-1 para parar):')
    if nome == "-1":
        break
    nomes.append(nome)
    idade= int(input('Digite a idade do cliente:'))
    idades.append(idade)
    if idade in range(0,6):
        precos.append(valor_ingresso*0.9)
        valores_desc.append( valor_ingresso * 0.9 )
        count_desc += 1
        count_10 +=1
    elif idade in range(6,13):
        precos.append( valor_ingresso * 0.92)
        valores_desc.append( valor_ingresso * 0.92)
        count_desc += 1
    elif idade in range(13,25):
        precos.append(valor_ingresso * 0.95)
        valores_desc.append( valor_ingresso * 0.95)
        count_desc += 1
    elif idade > 60:
        precos.append(valor_ingresso*0.85)
        valores_desc.append( valor_ingresso * 0.85)
        count_desc += 1
        idosos.append(nome)
    else:
        precos.append(valor_ingresso)

print("-"*50)

for x,y,z in zip(nomes,idades,precos):
    print(f'{x} tem  {y} anos e pagou R${z:.2f}')
print("-"*50)
print(f'{count_desc} pessoas tiveram desconto.')
print("-"*50)
print('RELAÇÃO IDOSOS!')
for i in idosos:
    print(i)

print("-"*50)
print(f'A média de valor dos descontos aplicados foi de {round(mean(valores_desc),2)}')
