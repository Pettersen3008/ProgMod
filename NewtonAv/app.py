from datetime import *
import matplotlib.pyplot as plt
import numpy as np

# Konstant


dt = 0.5 # 30 min
M_tid = 12 # hvor mange timer vi skal beregnde
M_temp = -30
k = -0.29 # h * a = k
T_kropp = 37 # temp kropp
T_ute = 8 # temp ute

dt = timedelta(minutes=30) # 30 min

# Lager liste for t
T = []

# Eulers
def euler(forrige, deriv, dt):
    '''Eulers metode for å estimere neste verdi i en tidsserie'''
    return forrige + k * (forrige - T_ute)  * dt

def finn_TOD(temp_body, )


# While loop
while t[-1] < dt:
    # Regn ut neste S
    S_deriv = dQdt(S_est[-1], I_est[-1])
    S_est.append(euler(S_est[-1], S_deriv, dt))



# Plot
plt.title('Sander')

plt.legend('Hei')
plt.show()
