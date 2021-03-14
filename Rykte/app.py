import numpy as np
import matplotlib.pyplot as plt

# Modellparametre
t_max = 20 # Antall dager vi simulerer.
N = 1100 # Antall Personer
dt = 0.1

props = 0.0007
ryktek = 2
rykteu = N - ryktek

# Startverdier
R_0 = ryktek # Hvor mange som vet det
S_0 = rykteu # Hvor mange flere som kan få vite det
t_0 = 0

# Lister for å lagre beregnede verdier,
# initierer med startverdier
S_est = [S_0]
R_est = [R_0]
t = [t_0]


# Her lager jeg funksjonene

# Vi bruker eulers methode
def euler(forrige, deriv, dt):
    '''Eulers metode for å estimere neste verdi i en tidsserie'''
    return forrige + deriv * dt

# 1
def dRdt(ryktek, props, rykteu):
    '''Euler - Antall som er vet ryktet'''
    return ryktek * props * rykteu

# While loop
while t[-1] < t_max:
    # Regn ut neste R
    rykteu = 1100 - R_est[-1] 
    R_deriv = dRdt(R_est[-1], props, rykteu)
    R_est.append(euler(R_est[-1], R_deriv, dt))

    # Lagre tid og legge til endringen av tid
    t.append(t[-1] + dt)


# plot
plt.title("Rykte spredning")
plt.plot(t, R_est, label='Antall Personer')
plt.xlabel('Dager')
plt.ylabel('Antall Personer')
plt.legend()
plt.grid()

# Felles Show for å vise alle plottene i et program
plt.show()