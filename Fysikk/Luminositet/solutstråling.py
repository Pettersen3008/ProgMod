# Imports
import math

### Konstanter
sigma = 5.67 * (10**-8)


### Input data

# Sola s.228
P_sola = 3.85 * (10**26) # Solas utstrålings effekt for T(r)
r_sola = 6.96 * (10**8) # Solradiusen

### Funksjoner

# Tar n kvadratroten av et tall(num)
def rootN(num, n):
    return num ** (1/n)

# Regner ut T
def T4():
    return P_sola / (sigma * 4 * math.pi * (r_sola**2))

### Svar til oppgaver 

# Sola sin effektive temp med hjelp av stefans lov
print(rootN(T4(), 4))


