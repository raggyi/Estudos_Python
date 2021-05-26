import re
import random

MULTIPLIERS=[11, 10, 9, 8, 7, 6, 5, 4, 3, 2]


def validate(cpf) :
    cpf=only_numbers(cpf)
    try:
        if is_sequence(cpf):
            return False
    except:
        return False
    try:
        new_cpf=calculate_digit( cpf=cpf, digit=1)
        new_cpf=calculate_digit( cpf=new_cpf, digit=2)
    except Exception as e:
        return False
    if new_cpf == cpf:
        return True
    else:
        return False


def calculate_digit(cpf, digit) :
    if digit == 1 :
        multipliers=MULTIPLIERS[1 :]
        new_cpf=cpf[:-2]
    elif digit == 2 :
        multipliers=MULTIPLIERS
        new_cpf=cpf
    else :
        return None
    total=0
    for index, multiplier in enumerate( multipliers ) :
        total += int(cpf[index]) * multiplier
    digit=11 - (total % 11)
    digit=digit if digit <= 9 else 0
    return f'{new_cpf}{digit}'


def only_numbers(cpf) :
    return re.sub(r'[^0-9]', '', cpf)


def is_sequence(cpf):
    sequencia=cpf[0] * len(cpf)
    if sequencia == cpf:
        return True
    else:
        return False


def reorganize_cpfs(cpf):
    return f'{cpf[:3]}.{cpf[3 :6]}.{cpf[6 :9]}-{cpf[9 :11]}'

def generate_randoms():
    first_block=random.randint(100,999)
    second_block=random.randint(100, 999)
    third_block=random.randint(100, 999)
    start_cpf= f'{first_block}{second_block}{third_block}00'
    new_cpf=calculate_digit(cpf=start_cpf,digit=1)
    new_cpf=calculate_digit(cpf=new_cpf,digit=2)
    return new_cpf
