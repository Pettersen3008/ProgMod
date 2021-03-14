# Nødvendige Bibloteker
import numpy as np

# Input
Sted = str(input("Hvilket område vil du simulere? "))
Personer = int(input("Hvor mange personer tilhører {}? ".format(Sted)))
Hjemme = int(input("Hvor mange har hjemme(skole/kontor)? "))
Smittet = int(input("Hvor mange antar du er smittet (på/i) {} den siste uken? ".format(Sted)))
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
sigma = 1/3.5
dt = 1
t_max = Dager
I_max = []


class Skole:

    Sted = Sted
    N = N
    t_max

    # Startverdier
    hjemme = Hjemme # Det er folk som har hjemme skole så vi fjerner dem fra regningen
    R_0 = (beta/gamma) # Removed = (0.25)/(1/10)
    I_0 = 1 # Antall som er smittet
    E_0 = 1 # Antall som er i startfasen av smitten
    S_0 = (N - I_0 - R_0 - hjemme) # Alle som kan bli smittet
    t_0 = 0 # Endringen over tid


    # Lister for å lagre beregnede verdier,
    # initierer med startverdier
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
        return (-beta * S * I) / N

    # 2
    def dEdt(S, I, E):
        '''dE/dt - Antall dager smitten er utsatt'''
        return ((beta * S * I) / N) - (sigma * E)


    # 3 
    def dIdt(E, I):
        '''dI/dt - Antall som er smittet'''
        return (sigma * E) - (gamma * I)

    # 4
    def dRdt(I):
        '''dR/dt - Antall som har vært smittet'''
        return gamma * I

    # While loop
    while t[-1] < t_max:
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

    print("Dersom vi !ikke! følger Rektor sine råd blir {} smittet".format(high))