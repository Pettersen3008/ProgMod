# Nødvendige Bibloteker
import matplotlib.pyplot as plt
import numpy as np
from rektor import * 
from skole import *

p1 = Rektor()
p2 = Skole()

# Plot 
plt.figure

# Plot for Skole 
plt.subplot(211)
plt.title("Spredningen av Covid19 smitte (på/i) {}".format(p2.Sted))
plt.plot(p1.t, p1.S_est, label='Antall Personer')
plt.plot(p1.t, p1.I_est, label='Antall Smittet')
plt.plot(p1.t, p1.R_est, label='Antall som har vært smittet')
plt.xlabel('Øverste grafen er FHI sine anbefallinger')
plt.ylabel('Antall Personer')
plt.grid()
plt.legend(bbox_to_anchor=(0.0, 1.2, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)

# Plot for Rektor
plt.subplot(212)
plt.xlabel('Dager')
plt.ylabel('Antall Personer')
plt.plot(p2.t, p2.S_est, label='Antall Personer')
plt.plot(p2.t, p2.I_est, label='Antall Smittet')
plt.plot(p2.t, p2.R_est, label='Antall som har vært smittet')
plt.grid()

# Felles Show for å vise alle plottene i et program
plt.show()
