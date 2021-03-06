import matplotlib.pyplot as plt
import numpy as np
# Initialbetingelser
DELTA_T = 0.1 # Tid mellom hver beregning
MAX_TIME = 12 # Hvor mange timer skal vi beregne
NORMAL_BODY_TEMP = 37 # Normal kroppstemperatur
MIN_TEMP = -30 # Laveste temperatur som tillates av programmet
K = -0.29 # Proporsjonalitetskonstant, h*A i Newtons avkjølingslov
# Funksjoner
def sjekkInput(tekst, minimum, maximum):
    ''' Funksjon som validerer inndata.
        Inndata må være et tall mellom spesifisert minimum og maksimum
    '''
    while True:
        try:
            verdi = float(input(tekst))
        except ValueError:
            print("OBS: inndata må være et tall!")
            continue
        if verdi < minimum or verdi > maximum:
            print("Verdien må være mellom {} og {}".format(minimum, maximum))
            continue
        else:
            break
    return verdi

def euler(T_forrige, T_omgivelse, dt):
    '''Regner ut ny kroppstemperatur'''
    return T_forrige + K * (T_forrige - T_omgivelse) * dt

def finn_TOD(temp_body, temp_hist):
    '''Regner ut dødstidspunkt (Time of Death)'''
    for x in temp_hist:
        if x < temp_body:
            return temp_hist.index(x) * DELTA_T

temp_omgivelse = sjekkInput('Omgivelsestemperatur: ', MIN_TEMP, NORMAL_BODY_TEMP)
temp_kropp = sjekkInput('Kroppstemperatur: ', temp_omgivelse, NORMAL_BODY_TEMP)

# Initierer to lister der verdiene for tid og temperatur lagres
t_hist = np.arange(0, MAX_TIME, DELTA_T).tolist() # Fyller listen med t-verdier
temp_hist = [NORMAL_BODY_TEMP]
# Hovedløkka som kjører eulerberegningen og skriver ut kroppstemperatur for hver DELTA_T
for i in t_hist:
    # temp_hist[-1] henter siste verdi fra lista temp_hist. Dette er y_forrige.
    temp_hist.append(euler(temp_hist[-1], temp_omgivelse, DELTA_T))
    if i % 0.5 == 0:
        print('Tid: {} timer. Temperatur: {} grader celcius.'.format(i, "%.2f" % temp_hist[-1]))
t_hist.append(t_hist[-1] + DELTA_T) # Legger til siste verdi for at listene skal bli like lange.
try:
    tod = finn_TOD(temp_kropp, temp_hist)
    title = 'Personen døde for {} timer siden.'. format(round(tod, 1))
except TypeError:
    title = 'Personen døde for mer enn {} timer siden.'. format(MAX_TIME)
# Utskrift til skjerm
plt.grid()
plt.title(title)
plt.xlabel('Tid [h]', fontsize=12)
plt.ylabel('Temperatur [°C]', fontsize=12)
plt.plot(t_hist,temp_hist, label='Euler, $\\Delta t = {}$ timer'.format(DELTA_T))
plt.axhline(y=NORMAL_BODY_TEMP, color='g', linestyle='-', label='Normal kroppstemperatur')
plt.scatter(0, NORMAL_BODY_TEMP, color='g')
plt.axhline(y=temp_kropp, color='r', linestyle='-', label='Temp når kroppen ble funnet')
plt.scatter(tod, temp_kropp, color='r')
plt.legend()
plt.grid(True, color='silver', linestyle='dashed', linewidth=1, axis='both')
plt.show()
