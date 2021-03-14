# Nødvendige Bibloteker
import matplotlib.pyplot as plt

# Input
Sted = str(input("Hvilket område vil du simulere? "))
Personer = int(input("Hvor mange personer tilhører {}? ".format(Sted)))
Smittet = int(input("Hvor mange antar du er smittet (på/i) {} idag? ".format(Sted)))
Dod = int(input("Hvor mange har vært smittet (på/i) {}? ".format(Sted)))
Dager = int(input("Hvor mange dager vil du simulere? "))

# Beta function
options = ["lite", "middels", "stor"]

# Printer ut valgene mine med tall
for i in range(len(options)):
    print(str(i+1) + ":", options[i])

Tetthet = int(input("Hvor tett er dere på {}? ".format(Sted)))

# Lagrer verdien til beta
if Tetthet == 1:
    beta = 0.25
elif Tetthet == 2:
    beta = 0.37
elif Tetthet == 3:
    beta = 0.50

# Sørger for at du velger et av alternativene over
if Tetthet in range(1, 4):
    Tetthet = options[Tetthet-1]
else:
    print("Velg et av tallene over!")


# Konstant Verdier
Sted = Sted
N = Personer
I = Smittet
R = Dod
gamma = 1/10
dt = 1
t_max = Dager

# Startverdier
R_0 = (beta/gamma)
I_0 = I
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

# Plot hentet fra tidligere Covid19 kode på github av Rune Mathisen: https://github.com/bitjungle/covid-19
plt.title("Spredningen av Covid19 smitte (i/på) {}, $N={:5.0f}$\n SIR model, $\\beta={:5.2f}$ $\\gamma={:5.2f}$ $R_0={:5.2f}$".format(Sted, N, beta, gamma, R_0))
plt.plot(t, S_est, label='Antall Personer som kan bli smittet')
plt.plot(t, I_est, label='Antall Personer som er smittet')
plt.plot(t, R_est, label='Antall Personer som har vært smittet')
plt.grid()
plt.xlabel('Dager')
plt.ylabel('Antall Personer')
plt.legend
plt.show()
