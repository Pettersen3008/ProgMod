'''
Reminder !!! 

Meningen med denne tanken er å sette inn mulige input og pygame for kart

Pygame = {
    Sette inn kart som på myharitage eller noe som viser hvor du befinner deg og en fin layout!

    Kilder: 
    https://github.com/saiduc/PyOpenGLobe
    https://github.com/afourmy/pyEarth
    https://github.com/brython-dev/brython/blob/master/www/gallery/pygame/chimp.html
    https://analyticsindiamag.com/top-9-python-frameworks-for-game-development/
    https://www.panda3d.org/features/ <- -> 

    https://stackoverflow.com/questions/53484453/can-we-use-python-with-react
    # Eller Pygame og Django ? 


    Bilder:
    https://www.google.com/search?q=pygame+3d+world+map&sxsrf=ALeKk01W-ej5ifQzBsco95W5aHyWSUtGlg:1611789160988&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjgtJLDnr3uAhUBzaQKHUPWCbQQ_AUoAXoECAYQAw&biw=1680&bih=946


    Rune:
    lage diagram: "hvis vi bruker munnbind hvordan blir grafen?"
    "hvis vi er færre hvordan blir det da"
    "hvor viktig meteren er"



    !NBBBBBB Sjekk ut dash python visualisation


    Kanskje lage en nettside som sender data til python og lagrer dette tar et skjermbilde og laster det opp til nettsiden eller noe sånt?
    Hvertfall en nettsiden med disse spørsmålene. Kan lage det i javascript også men er litt gøy med python
}
'''



# Nødvendige Bibloteker
import matplotlib.pyplot as plt

# Input
Sted = str(input("Hvilket område vil du simulere? "))
Personer = int(input("Hvor mange personer tilhører {}? ".format(Sted)))
Smittet = int(input("Hvor mange antar du er smittet på {} idag? ".format(Sted)))
Dod = int(input("Hvor mange har vært smittet på {}? ".format(Sted)))
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
#plt.title("Spredningen av Covid19 smitte på $N={:5.0f}, $N={:5.0f}$\n SIR model, $\\beta={:5.2f}$ $\\gamma={:5.2f}$ $R_0={:5.2f}$".format(Sted, N, beta, gamma, R_0))
plt.plot(t, S_est, label='Susceptible')
plt.plot(t, I_est, label='Infectious')
plt.plot(t, R_est, label='Removed')
plt.grid()
plt.xlabel('Dager')
plt.ylabel('Antall Personer')
plt.legend
plt.show()
