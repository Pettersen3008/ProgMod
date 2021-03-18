'''
En gammel legende sier at oppfinneren av sjakkspillet solgte oppfinnelsen sin til landets hersker. 
Som betaling ville han ha:
1 riskorn for den første ruta på sjakkbrettet
2 riskorn for den andre ruta
4 riskorn for den tredje ruta
8 riskorn for den fjerde ruta
...også videre. 

Et sjakkbrett har 8 rader og 8 linjer. 
Lag et program som besvarer disse to oppgavene:

a)Hvor mange riskorn bli det totalt?
b)På hvilken rute passerer vi 1.000.000 riskorn?
'''

import numpy as np
import math

# Printer ut et sjakk brett i terminalen
board = np.zeros((8,8))


# Liste for rutene som er solgt
solgt = [] 


def funk(x):
    return x * x

for x in range(1, 65):
    print(funk(x))

print(128 * 128)