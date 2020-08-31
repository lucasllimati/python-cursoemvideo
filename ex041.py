# EXERCÍCIO 4
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

from datetime import date

anonasc = int(input('Digite o ano de nascimento: '))
anoatual = date.today().year
idadecat = anoatual - anonasc
print('O atleta tem {} anos.'.format(idadecat))

if idadecat <= 9:
    print('Classificação: \33[36mMIRIM\33[m.')
elif 9 < idadecat <= 14:
    print('Classificação: \33[36mINFANTIL\33[m.')
elif 14 < idadecat <= 19:
    print('Classificação: \33[36mJÚNIOR\33[m.')
elif 19 < idadecat <= 25:
    print('Classificação: \33[36mSÊNIOR\33[m.')
else:
    print('Classificação: \33[36mMASTER\33[m.')

