from collections import Counter

Cpfs = []
nomes = []
idades = []
convenio = False
idoso_com_convenio = []
precos = [250,150,200,150,200]
valores_pagos = []
servicos= []

while True:
    cpf = input('Digite o Cpf do cliente(-1 se não tiver mais clientes): ')
    if int(cpf) == -1:
        break
    Cpfs.append(cpf)
    nome=input('Digite o nome do cliente : ')
    nomes.append(nome)
    idade =int(input('Digite a idade do cliente: '))
    idades.append(idade)

    verifica_convenio = input('O cliente tem convênio?(S/N): ')
    if verifica_convenio.upper() == 'S':
        convenio = True
    else:
        convenio = False
    if convenio and idade > 59:
        idoso_com_convenio.append(nome)
    servico= input('Qual tipo de médico o cliente foi  '
                   '\n[1]Clínico Geral'
                   '\n[2]Nutricionista'
                   '\n[3]Fonoaudiólogo'
                   '\n[4]Fisioterapeuta'
                   '\n[5]Odontólogo'
                   '\n')
    servicos.append(servico)
    if servico == '1':
        valor_pago =precos[0]
    elif servico == '2':
        valor_pago =precos[1]
    elif servico =='3':
        valor_pago=precos[2]
    elif servico == '4':
        valor_pago=precos[3]
    else:
        valor_pago = precos[4]
    if convenio:
        valor_pago = valor_pago * 0.25
        valores_pagos.append(valor_pago)
    else:
        valores_pagos.append(valor_pago)

print(50 * '-')#letra a

for k,v in Counter(servicos).items():
    if k == '1':
        k = 'Clinico Geral'
    elif k ==' 2':
        k = 'Nutricionista'
    elif k == '3':
        k = 'Fonoaudiólogo'
    elif k == '4':
        k = 'Fisioterapeuta'
    else:
        k= 'Odontólogo'
    print(f'{k} atendeu: {v} clientes.')


print(50 * '-') #letra b

print('RELAÇÃO IDOSOS COM CONVENIO')
for i in idoso_com_convenio:
    print(i)

print(50 * '-')#letra c
print(f'{servicos.count("4")/len(servicos) *100}% dos clientes foram ao fisioterapeuta')
print(50 * '-')#letra d

print(f'A clinica arrecadou ao final do expediente : R${sum(valores_pagos)}')

print(50 * '-')