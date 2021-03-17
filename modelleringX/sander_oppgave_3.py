import matplotlib.pyplot as plt

# Konstanter

dt = 0.01
r = 0.37 # Prosentfaktoren

t_0 = 1 # Dag = 1
t_max = 200 # Antall dager
k_0 = 2500 # Max individer
P_0 = 100 # Antall kaninger vi starter med

# Lager liste for å lagre beregnede verdier
# Her legger jeg også til startverdier
K_est = [k_0]
P_est = [P_0]
t = [t_0]

# Eulers 
def euler(forrige, deriv, dt):
    '''Eulers metode for å estimere neste verdi i en tidsserie'''
    return forrige + deriv * dt

# Delta P
def dPdt(P, k):
    ''' regner ut delta P '''
    return(r*P)*(1-(P/k))


# Lopp igjenom til
while t[-1] < t_max:
    # Regn ut neste P
    P_deriv = dPdt(P_est[-1], K_est[-1])
    P_est.append(euler(P_est[-1], P_deriv, dt))

    # Lagre tid og legge til endringen av tid
    t.append(t[-1] + dt)


print(P_est)

# Plot
plt.figure()
plt.title('Kaniner')
plt.xlabel('Dager')
plt.ylabel('Antall kaniner')
plt.plot(t, P_est, label='Spredning av kaniner')
plt.show()