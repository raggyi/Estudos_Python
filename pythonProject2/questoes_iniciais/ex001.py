from collections import Counter
cpfs=[]
precinhos = {
    100: 4.20,
    101: 7.30,
    102: 8.50,
    103: 9.20,
    104: 10.30,
    105: 8
}
compras=[]
motoboy=[]
while True:
    cod = int(input('Digite o código do pedido'
                    "\n Cachorro Quente 100 "
                    "\n BauruSimples 101"
                    " \n Bauru com ovo 102"
                    "\n Hambúrguer 103"
                    "\n Cheeseburguer 104"
                    "\n Refrigerante 105" 
                    "\n (Digite -1 para parar) "':'))
    if cod == -1:
        break
    qtd = int(input('Digite a qtd de itens:'))
    frete =int((input('Digite o valor do Frete:')))
    frete_motoboy= frete*0.6
    motoboy.append(frete_motoboy)
    compras.append(precinhos[cod] * qtd +frete)
i=0
while i < len(motoboy):
    cpf =int((input('Qual o Cpf do cliente:')))
    i=i+1
    cpfs.append(cpf)
print(f'O pedido com o maior valor pago:R${max(compras)}') #questao a
print(f'O pedido com o maior valor pago:R${min(compras)}') #questao b
print(f'O motoboy arrecadou no final do expediente:R${sum(motoboy)}') #questao c
print(f'O dono do Eggs lanches faturou:R${sum(compras)-sum(motoboy)}') #questao d"