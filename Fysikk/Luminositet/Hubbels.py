### Imports
import matplotlib.pyplot as plt
from uncertainties import ufloat
import math

### Konstanter
# v = int(input("Hvor stor fart har objektet ? "))

v = 1.2 * (10**7)
H = (21.7 * (10**3)) / (10**6) * 1 # m/s 1.y
r = v / H

### Funksjoner

# Høyeste verdi av Hubbels
def H_max():
    return (22.7 * (10**3)) / (10**6) * 1 # m/s 1.y

# Laveste verdi av Hubbels
def H_min():
    return (20.7 * (10**3)) / (10**6) * 1 # m/s 1.y

def r_max():
    return (v / H_min()) * (10**6)

def r_min():
    return (v / H_max()) * (10**6)

print("r_min =", r_min())
print("r_max =", r_max())
