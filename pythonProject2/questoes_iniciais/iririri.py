dias={
    'segunda':0,
    'terça':0,
    'quarta':0,
    'quinta':0,
    'sexta':0
}
placas=[]
veiculos=int((input('Digite o número de carros a serem cadastrados:')))
dia_mais=0
qtd_mais=-1
for i in range(veiculos):
    n=int(input('Digite o número da sua placa(Entre 1 e 9999:'))
    if n > 9999:
        print('A sua placa tem que ser entre 1 e 9999')
        n = int(input('Digite o número da sua placa(Entre 1 e 9999:'))
    placas.append(n)
    if str(placas[i])[-1] == "1" or str(placas[i])[-1] == "2" :
        dias['segunda']+=1
    elif str(placas[i])[-1] == '3' or str(placas[i])[-1] == '4':
        dias['terça'] += 1
    elif str(placas[i])[-1] == '5' or str(placas[i])[-1] == '6':
        dias['quarta'] += 1
    elif str(placas[i])[-1] == '7' or str(placas[i])[-1] == '8':
        dias['quinta'] += 1
    else:
        dias['sexta'] += 1
for key,value in dias.items():
    if value > qtd_mais:
        qtd_mais=value
        dia_mais=key
print(f'Quantida de carros barrados na segunda e na terça:',dias['segunda']+dias['terça'])
print(f'Porcentagem de carros permitidos na sexta', (((len(placas)-dias['sexta'])/len(placas)) * 100),'%')
print(f'O dia com mais carros com restrição foi {dia_mais} e {qtd_mais} são bloqueados nesse dia')
