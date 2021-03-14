# Nødvendige Bibloteker
import matplotlib.pyplot as plt


# Modellparametre
beta = 0.25 # Kontakt mellom smitte og motakker
gamma = 1/10 # Tid det tar å bli friskt
dt = 1 # Endringen av tid
t_max = 100 # Antall dager vi simulerer.
N = 1100 # Antall Personer

# Startverdier
R_0 = (beta/gamma)
I_0 = 10
S_0 = (N - I_0 - R_0)
t_0 = 0

# Lister for å lagre beregnede verdier,
# initierer med startverdier
S_est = [S_0]
I_est = [I_0]
R_est = [R_0]
t = [t_0]

# Eulers 
def euler(forrige, deriv, dt):
    '''Eulers metode for å estimere neste verdi i en tidsserie'''
    return forrige + deriv * dt

# 1
def dSdt(S, I):
    '''dS/dt - Susceptible'''
    return (-beta * S * I) / N

# 2 
def dIdt(S, I):
    '''dI/dt - Infectious'''
    return (beta * S * I) / N - gamma * I

# 3
def dRdt(I):
    '''dR/dt - Removed'''
    return gamma * I

# While loop
while t[-1] < t_max:
    # Regn ut neste S
    S_deriv = dSdt(S_est[-1], I_est[-1])
    S_est.append(euler(S_est[-1], S_deriv, dt))

    # Regn ut neste I
    I_deriv = dIdt(S_est[-1], I_est[-1])
    I_est.append(euler(I_est[-1], I_deriv, dt))

    # Regn ut neste R
    R_deriv = dRdt(I_est[-1])
    R_est.append(euler(R_est[-1], R_deriv, dt))

    # Lagre tid og legge til endringen av tid
    t.append(t[-1] + dt)

# Pyplot 
# plt.plot(t, S_est)
# plt.plot(t, I_est)
# plt.plot(t, R_est)
# plt.show()

plt.title("Spredningen av Covid19 smitte på Skien Vidregående Skole, $N={:5.0f}$\n SIR model, $\\beta={:5.2f}$ $\\gamma={:5.2f}$ $R_0={:5.2f}$".format(N, beta, gamma, R_0))
plt.plot(t, S_est, label='Susceptible')
plt.plot(t, I_est, label='Infectious')
plt.plot(t, R_est, label='Removed')
plt.grid()
plt.xlabel('Days')
plt.ylabel('Number of people')
plt.legend
plt.show()