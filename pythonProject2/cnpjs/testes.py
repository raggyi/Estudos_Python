import funcoes
cnp1='aaaaaaaa'
cnpj_random=funcoes.formata(funcoes.gera())
if funcoes.valida(cnpj_random):
    print(f'o CNPJ {cnpj_random} é Válido')
else:
    print( f'o CNPJ {cnpj_random} é Inválido' )