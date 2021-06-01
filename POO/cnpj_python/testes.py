import funcoes
cnpj1="90.400.888/0001-43"
cnpj_random=funcoes.formata(funcoes.gera())
if funcoes.valida(cnpj_random):
    print(f'Esse cnpj {cnpj_random} é Válido')
else:
    print( f'Esse cnpj {cnpj_random} é Inválido' )
print(funcoes.gera())