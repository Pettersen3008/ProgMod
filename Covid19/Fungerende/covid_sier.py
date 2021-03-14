# Nødvendige Bibloteker
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np

# Startverdier for R0
date_today = datetime.today()
tmax = 365 # Antall dager
R_0 = 3.08 # R0
t = 0 # Endringen over tid

# Modellparametre
N = 1200 # Antall 
gamma = 1/10 # Tid det tar å bli friskt
beta = R_0 * gamma # Kontakt mellom smitte og motakker
sigma = 1/3.5 # Antall dager som det tar fra du er smitta til du er smittsom
alpha = 1/5.1 # Antall dager før du får symtomer på corona
dt = 1 # Endringen av tid
I_max = [] # Liste for høyeste antall mennesker som er syke samtidig
u = 0.3 # Er hastigheten vi møter de smittede på.

# Startverider = Felles
R_0 = (beta/gamma)
E_0 = 1/200
I_0 = 1
S_0 = (N - E_0 - I_0 - R_0)
t_0 = 0

# Lister for å lagre beregnede verdier,
# initierer med startverdier = Felles
S_est = [S_0]
E_est = [E_0]
I_est = [I_0]
R_est = [R_0]
t = [t_0]

# Eulers 
def euler(forrige, deriv, dt):
    '''Eulers metode for å estimere neste verdi i en tidsserie'''
    return forrige + deriv * dt

# 1
def dSdt(S, I):
    '''dS/dt - Antall som har muligheten til å bli smittet'''
    return (-(1-u) * beta * S * I) / N

# 2
def dEdt(S, I, E):
    '''dE/dt - Antall dager smitten er utsatt'''
    return (((1-u) * beta * S * I) / N) - (sigma * E)


# 3 
def dIdt(E, I):
    '''dI/dt - Antall som er smittet'''
    return (sigma * E) - (gamma * I)

# 4
def dRdt(I):
    '''dR/dt - Antall som har vært smittet'''
    return gamma * I


# While loop
while t[-1] < tmax:
    # Regn ut neste S
    S_deriv = dSdt(S_est[-1], I_est[-1])
    S_est.append(euler(S_est[-1], S_deriv, dt))

    # Regn ut neste E
    E_deriv = dEdt(S_est[-1], I_est[-1], E_est[-1])
    E_est.append(euler(E_est[-1], E_deriv, dt))

    # Regn ut neste I
    I_deriv = dIdt(E_est[-1], I_est[-1])
    I_est.append(euler(I_est[-1], I_deriv, dt))

    # Regn ut neste R
    R_deriv = dRdt(I_est[-1])
    R_est.append(euler(R_est[-1], R_deriv, dt))

    # Lagre tid og legge til endringen av tid
    t.append(t[-1] + dt)

for I_est[-1] in I_est:
    if I_est[-1] > I_est[-2]:
            I_max.append(I_est[-1])
            high = (round(np.amax(I_max)))

plt.title("Spredningen av Covid19 smitte på Skien Vidregående Skole, $N={:5.0f}$\n SIR model, $\\beta={:5.2f}$ $\\gamma={:5.2f}$, sigma=${:5.2f}$, $R_0={:5.2f}$".format(N, beta, gamma, sigma, R_0))
plt.plot(t, S_est, label='Antall Personer')
plt.plot(t, I_est, label='Antall Smittet')
plt.plot(t, R_est, label='Antall som har vært smittet')
plt.xlabel('Dager')
plt.ylabel('Antall Personer')
plt.legend(bbox_to_anchor=(0.0, 1.2, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)
plt.grid()
plt.show()
