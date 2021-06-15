import random
letras= ['A','B','C','D']
lista=[]
cont = 0
for i in range(127):
    lista.append(random.choice(letras))
    valores= random.randint(40000,100000)
    lista.append(valores)
    if valores < 75000:
        cont+=1
print(f'{lista.count("A")} Projetos Ótimos')
print(f'{lista.count("D")} Projetos Ruins')
print(f'{round(((lista.count("A")+lista.count("B"))/(len(lista))*100 ),2)}% dos projetos foram bons ou ótimos')
print(f'{cont} projetos tiveram o orçamento menor de que R$75000,00')