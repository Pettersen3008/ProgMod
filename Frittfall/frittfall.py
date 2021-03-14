import numpy


# --- konstanter ---
g = 9.81    # m/s^2
m = 80      # kg
k = 0.24    # kg/m
v0 = 0      # m/s
h0 = 3000   # m


# --- Simuleringsparameter ---
dt = 1.0    # s


# --- Lagre alle beregnede verider i lister ---
v = [v0]  # Fart
h = [h0]  # Høyde
t = [0]   # Tida som har gått


# --- Eulers metode ---

def ny_fart(v, dt):
    '''
    Bruker Eulers metode til å beregne ny fart 
    '''
    return v + (g - (k/m) * v**2) * dt


def ny_hoyde(h, v, dt):
    return h - v * dt

while h[-1] > 0:
    v.append(ny_fart(v[-1], dt))
    h.append(ny_hoyde(h[-1], v[-1], dt))
    t.append(t[-1] + dt)

print(v)
print(h)