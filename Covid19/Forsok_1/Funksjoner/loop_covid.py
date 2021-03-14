import numpy as np

# Funskjon for range med desimaltall
def drange2(start, stop, step):
    num = int((stop-start)/float(step))
    for i in range(num+1):
        yield start + i*step

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

# Modellparametre
beta = 0.25 # Kontakt mellom smitte og motakker
gamma = 1/10 # Tid det tar å bli friskt
sigma = 1/3.5 # Antall dager som det tar fra du er smitta til du er smittsom
dt = 1 # Endringen av tid
t_max = 365/2 # Antall dager vi simulerer.
I_max = []
N = 1200 # Antall 

# Startverider = Felles
R_0 = (beta/gamma)
E_0 = 1
I_0 = 1
S_0 = (N - I_0 - R_0)
t_0 = 0

for i in drange2(0, 1, 0.05):
    beta = round(i, 2)

    # Lister for å lagre beregnede verdier,
    # initierer med startverdier = Felles
    S_est = [S_0]
    E_est = [E_0]
    I_est = [I_0]
    R_est = [R_0]
    t = [t_0]
    
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

    print("beta = {} \nhøyeste smittet = {} \n".format(beta, high))


#print("E_0 = {} \nI_0 = {}".format(E_0, I_0))