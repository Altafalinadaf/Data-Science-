import math
import pydoc

pydoc.help()

def fac(n):
    return math.factorial(n)

n=int(input('enter the number : '))

print(f'{n} factorail is {fac(n)}')

