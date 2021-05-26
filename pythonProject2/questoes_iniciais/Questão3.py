cnh_do_cara = []
qtd_pontos_registrados = []
qtd_infracoes_graves = []
validacao = ""
cont_30 = 0
cont_20 = 0
cont_40 = 0
soma = 0
while True:
    cnh = input('Digite o número de sua CNH: ')
    cnh_do_cara.append(cnh)
    pontos = int(input('Digite a quantidade de pontos registrados:'))
    qtd_pontos_registrados.append(pontos)
    infracoes_graves = int(input('Digite a quantidade de infrações gravíssimas:'))
    qtd_infracoes_graves.append(infracoes_graves)
    validacao=input('Digite S se quiser continuar e N se deseja parar:')
    if validacao in "SssimSimSIM":
        continue
    else:
        break
for i in range(len(cnh_do_cara)):
    if qtd_infracoes_graves[i] == 1 and qtd_pontos_registrados[i] >= 30:
        cont_30 += 1
    elif qtd_infracoes_graves[i] == 0 and qtd_pontos_registrados[i] >= 40:
        cont_40 += 1
    elif qtd_infracoes_graves[i] >= 2 and qtd_pontos_registrados[i] >= 20:
        cont_20 += 1
for i in qtd_pontos_registrados:
    soma += i



print(soma)
print(cont_30)
print(cont_20 / (cont_30+cont_40+cont_20) * 100)
print(soma / len(cnh_do_cara))