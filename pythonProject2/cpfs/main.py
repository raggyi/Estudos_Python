import functions
cpf='103.314.770-25'
cpf=functions.reorganize_cpfs(functions.generate_randoms())
if functions.validate(cpf):
    print(f'{cpf} é  Válido')
else:
    print(f'{cpf} é Inválido')
