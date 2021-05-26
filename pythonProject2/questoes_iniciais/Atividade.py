from random import sample
from random import randint

sorterated=[]
surpresinha=sample(range(1,25),18)
surpresinha1=sample(range(1,25),18)
choices=[]
count_choices=0
count_surpresinha=0
count_surpresinha1=0
for i in range(18):
    s=randint(1,25)
    sorterated.append(s)

qtd=int(input('Digite quantos números você deseja apostar(Entre 15 e 18):'))
if qtd not in range(14,19):
    print('Por favor digite um número entre 15 e 18')
    qtd=int( input( 'Digite quantos números você deseja apostar(Entre 15 e 18):'))

while len(choices)<qtd:
    num=int(input('Digite seu número entre 01 e 25:'))
    if num not in range(1,26):
        print('Precisa ser um numero entre 1 e 25')
        num=int( input( 'Digite seu número entre 01 e 25:' ) )
    if num in choices:
        print( 'Precisa ser um numero entre 1 e 25' )
        num=int( input( 'Digite seu número entre 01 e 25:'))
    choices.append(num)

for i in range(len(choices)):
    if choices[i] in sorterated:
        count_choices += 1

for i in range(len(surpresinha)):
    if surpresinha[i] in sorterated:
        count_surpresinha += 1
    if surpresinha1[i] in sorterated:
        count_surpresinha1 += 1

print(sorted(choices))
print(sorted(surpresinha))
print(sorted(surpresinha1))
print(sorted(sorterated))
print(f'As apostas escolhidas acertaram {count_choices} númereros')
print(f'As surpresinhas acertaram {count_surpresinha} e {count_surpresinha1} números')