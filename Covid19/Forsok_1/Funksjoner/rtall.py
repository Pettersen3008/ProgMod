from datetime import date
# Startverdier for datoer og R0
startdato = date(2020, 2, 17)
R0 = 3.08
rtall = {
    0: R0, # Dette er R0-tallet for 2020-02-17
    (date(2020, 3, 15) - startdato).days: 0.53,
    (date(2020, 4, 20) - startdato).days: 0.56,
    (date(2020, 5, 11) - startdato).days: 0.59,
    (date(2020, 7, 1) - startdato).days: 0.72,
    (date(2020, 8, 1) - startdato).days: 1.03,
    (date(2020, 9, 1) - startdato).days: 0.97,
    (date(2020, 10, 1) - startdato).days: 1.23,
    (date(2020, 10, 26) - startdato).days: 1.47,
    (date(2020, 11, 5) - startdato).days: 0.83,
    (date(2020, 12, 1) - startdato).days: 1.07,
    (date(2021, 1, 4) - startdato).days: 0.65
}
t = 0 # Teller for antall dager etter startdatoen
tmax = 365/2 # Vi kjører simuleringen i ett år 
while t < tmax:
    if t in rtall: # Er det et nytt R0-tall for denne dagen?
        R0 = rtall[t]
        print(' {} etter {} dager'.format(R0, t))
    # Her kan du kjøre simuleringsmodellen din...
    t += 1 # Vi teller oss fram en dag