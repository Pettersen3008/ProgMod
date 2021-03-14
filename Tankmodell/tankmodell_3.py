import math # vi trenger dette biblioteket senere

A_t = 2.00  # Tankens tverrsnittareal (m^2)
A_h = 0.002 # Hullets tverrsnittareal (m^2)
h = 4.00    # Vannivået når forsøket starter (m)
g = 9.81    # Gravitasjonskonstanten (m/s^2)

V0 = A_t * h
print("Volumet ved tiden t = 0 s er {} m^3".format(V0))

C = 1
k = C * math.sqrt(2*g)
print("Konstanten k er {}".format(k))

def euler(h, dh, dt):
    '''
    Regner ut ny høyde i tanken vet tiden t+dt,
    er
    ''' 

    return h + dh * dt

def stigning(A_h, A_t, h):
    return - (A_h / A_t) * k * math.sqrt(h)import math # vi trenger dette biblioteket senere

A_t = 2.00  # Tankens tverrsnittareal (m^2)
A_h = 0.002 # Hullets tverrsnittareal (m^2)
h = 4.00    # Vannivået når forsøket starter (m)
g = 9.81    # Gravitasjonskonstanten (m/s^2)

def hastighet(h):
    if h > 0.0:
        return k * math.sqrt(h)
    else:
        return 0.0

t = 0   # starttiden
dt = 15 # tidssteg i sekunder
h_lim = 0.02 # vi stopper beregningen når høyden er mindre enn denne
t_hist = [] # Lagerplass for historiske tidspunkter
h_hist = [] # Lagerplass for historiske h-verdier
while h > h_lim:
    if t > 0: # ingen beregning ved t = 0, der bruker vi initialverdier
        h = euler(h, stigning(A_h, A_t, h), dt)
    v = hastighet(h) # Hastigheten til væsken som strømmer ut av hullet
    q_ut = A_h * v # Mengden væske som strømmer ut av hullet
    print("t = {} => h = {} \t v = {} \t qut = {}".format(t, round(h,2), round(v,2), round(q_ut,4)))
    t_hist.append(t)
    h_hist.append(h)
    t += dt # tidspunkt ved neste tidssteg

import matplotlib.pyplot as plt
plt.plot(t_hist, h_hist)
plt.ylabel('Høyde [m]')
plt.xlabel('Tid [s]')
plt.grid()
plt.show()