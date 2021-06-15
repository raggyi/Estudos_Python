atendimentos=[]

while True :
    codigo=int( input(
        "Digite o código do atendimento ou -1 para  sair [1: Clínico Geral, 2: Nutricionista, 3: Fonoaudiológo, 4: Fisioterapeuta, 5: Odontólogo]: " ) )

    if codigo == -1 :
        codigos=[i["codigo"] for i in atendimentos]
        print(
            f"\nAtendimentos do dia: Clínico geral — {codigos.count( 1 )} atendimento(s) | Nutricionista — {codigos.count( 2 )} atendimento(s) | Fonoaudiologia — {codigos.count( 3 )} atendimento(s) | Fisioterapeuta — {codigos.count( 4 )} atendimento(s) | Odontologia — {codigos.count( 5 )} atendimento(s)" )

        relacao_nominal=[i["nome"] for i in atendimentos if i["tem_convenio"] == True and i["idade"] > 59]
        print( "Relação dos pacientes com convênio e com idade maior de 59: ", relacao_nominal )

        pacientes_para_fisioterapia=codigos.count( 4 ) / len( atendimentos ) * 100
        print(
            f"Porcentagem de pacientes que realizaram procedimento com fisioterapeuta: {pacientes_para_fisioterapia:.2f}%" )

        valor_total=sum( i["valor"] for i in atendimentos )
        print( "Valor total arrecadado pela clínica ao final do expediente: ", valor_total )
        break

    elif codigo <= 0 or codigo > 5 :
        print( "Escolha um atendimento válido. " )
        break

    else :
        cpf=input( "CPF do paciente: " )
        nome=input( "Nome do paciente: " )
        idade=int( input( "Idade do paciente: " ) )

        if codigo == 1 :
            valor=250
        elif codigo == 2 :
            valor=150
        elif codigo == 3 :
            valor=200
        elif codigo == 4 :
            valor=150
        elif codigo == 5 :
            valor=200

        tem_convenio=input( "Possui convênio? (S/N): " ).upper() == "S"

        if tem_convenio :
            valor=valor - valor * 0.75

        atendimento={
            "codigo" : codigo,
            "cpf" : cpf,
            "nome" : nome,
            "idade" : idade,
            "tem_convenio" : tem_convenio,
            "valor" : valor
        }

        atendimentos.append( atendimento )
print(atendimentos)