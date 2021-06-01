""" Try uses the same method as IF and Else.
try:
    a=1/0
    print(a)
except Exception as e:
    print('ERROR')
"""


"""Raise method is useless when you need to put your own ERROR message
def division(n1, n2, ) :
    if n2==0:
        raise ValueError( 'n2 cannot be 0 ' )
    return n1 / n2

print(division(1,0))

"""