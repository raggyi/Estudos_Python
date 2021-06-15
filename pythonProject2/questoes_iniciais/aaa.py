qtnd = 0
possuiconv = 0
finalclinico = 62.5
nomes = []
nutrifinal = fisiofinal = 37.5
fonofinal = odontofinal = 50
pacient59 = []
fisio = []
nutri = []
clini = []
fono = []
odonto = []
valorfinal1 = []
final2 = [250,200,150]
valorfinal2 = []
n = fi = 150
cg = 250
fo = odo = 200
convenio = "N"
while True:
  cpf = int(input("CPF: "))
  if cpf == -1:
      break
  nome = str(input("NOME: "))
  qtnd = qtnd + 1
  nomes.append(nome)
  idade = int(input("IDADE: "))
  print("CLÍNICO GERAL DIGITE 1")
  print("NUTRICIONISTA DIGITE 2")
  print("FONOAUDIÓLOGO DIGITE 3")
  print("FISIOTERAPEUTA DIGITE 4")
  print("ODONTOLOGO DIGITE 5")
  perg = int(input("DIGITE O NÚMERO DE ACORDO COM O ESPECIALISTA QUE DESEJA: "))
  if perg == 4:
      fisio.append(perg)
  if perg == 1:
      clini.append(perg)
  if perg == 2:
      nutri.append(perg)
  if perg == 5:
      odonto.append(perg)
  if perg == 3:
      fono.append(perg)
  conv = str(input("POSSUI CONVÊNIO(s/n): "))
  if conv.upper() != convenio and idade >= 59:
      pacient59.append(nome)
  if conv == "s" and perg == 1:
      valorfinal1.append(finalclinico)
  if conv == "s" and perg == 2:
      valorfinal1.append(nutrifinal)
  if conv == "s" and perg == 3:
      valorfinal1.append(fonofinal)
  if conv == "s" and perg == 4:
      valorfinal1.append(fisiofinal)
  if conv == "s" and perg == 5:
      valorfinal1.append(odontofinal)
  if conv == "n" and perg == 1:
      valorfinal2.append(final2[0])
  if conv == "n" and perg == 2:
      valorfinal2.append(final2[2])
  if conv == "n" and perg == 3:
      valorfinal2.append(final2[1])
  if conv == "n" and perg == 4:
      valorfinal2.append(final2[2])
  if conv == "n" and perg == 5:
      valorfinal2.append(final2[1])
x = (len(fisio))/(qtnd)*100
print("CLÍNICO GERAL", len(clini)) #LETRA A
print("NUTRICIONISTA", len(nutri)) #LETRA A
print("FONOAUDIÓLOGO", len(fono))  #LETRA A
print("ODONTOLOGO", len(odonto))   #LETRA A
print("FISIOTERAPEUTA", len(fisio))#LETRA A
print(f"A quantidades de pessoas registradas foi de {qtnd}") #LETRA A
print("CLIENTES QUE TEM CONVÊNIO E POSSUI MAIS DE 59 ANOS", pacient59) #LETRA B
print(f"PERCENTUAL DE PESSOAS QUE FIZERAM FISIOTERAPIA:{x:.2f}""%") #LETRA C
print(valorfinal1)
print(valorfinal2)
print("O VALOR TOTAL ARRECADADO PELA CLÍNICA É: R$", sum(valorfinal1) + sum(valorfinal2)) #LETRA D