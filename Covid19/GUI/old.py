# ----------------- Imports --------------------- #
import tkinter as Tkinter
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

# Lager winduet
root = Tkinter.Tk()

# Overskrift
Heading = Tkinter.Label(text="Covid-19 Simulation") #, font=BOLD)
Heading.pack(side="top")

# Lager et vindu for variabler
frame = Tkinter.Frame(root)
frame.pack(side="top")

# Her setter jeg en standard input for hver variabel som skal brukes til utregning senere
Place = Tkinter.StringVar()
Place.set("Skien")

Persons = Tkinter.StringVar()
Persons.set("1200")

HomeOffice = Tkinter.StringVar()
HomeOffice.set("6")

Infected = Tkinter.StringVar()
Infected.set("3")

Days = Tkinter.StringVar()
Days.set("100")

OptionList = {
    'Lite': 0.25,
    'Medium': 0.37,
    'Stor': 0.50
}

for opt in OptionList:
    print(OptionList[opt])

Density = Tkinter.StringVar()
Density.set(opt)

Option = Tkinter.OptionMenu(root, Density, *OptionList)
Option.config(width=8)
Option.pack(side="top")

# ----------------- Create row values --------------------- #
# Her lager jeg input feltene
row_counter = 0
Place_text = Tkinter.Label(frame, text="Hvilke område vil du simulere:") 
Place_text.grid(row=row_counter, column=0)

Place_entry = Tkinter.Entry(frame, width=8, textvariable=Place)
Place_entry.grid(row=row_counter, column=1)

row_counter += 1
Persons_text = Tkinter.Label(frame, text="Hvor mange er dere på område:") 
Persons_text.grid(row=row_counter, column=0)

Persons_entry = Tkinter.Entry(frame, width=8, textvariable=Persons)
Persons_entry.grid(row=row_counter, column=1)

row_counter += 1
HomeOffice_text = Tkinter.Label(frame, text="Hvor mange har hjemmekontor:") 
HomeOffice_text.grid(row=row_counter, column=0)

HomeOffice_entry = Tkinter.Entry(frame, width=8, textvariable=HomeOffice)
HomeOffice_entry.grid(row=row_counter, column=1)

row_counter += 1
Infected_text = Tkinter.Label(frame, text="Hvor mange er antatt smittet?:") 
Infected_text.grid(row=row_counter, column=0)

Infected_entry = Tkinter.Entry(frame, width=8, textvariable=Infected)
Infected_entry.grid(row=row_counter, column=1)

row_counter += 1
Days_text = Tkinter.Label(frame, text="Hvor mange dager vil du simulere:") 
Days_text.grid(row=row_counter, column=0)

Days_entry = Tkinter.Entry(frame, width=8, textvariable=Days)
Days_entry.grid(row=row_counter, column=1)

row_counter += 1
Density_text = Tkinter.Label(frame, text="Hvor stor avstand er det fra person til person:") 
Density_text.grid(row=row_counter, column=0)

Density_entry = Tkinter.Entry(frame, width=8, textvariable=Density)
Density_entry.grid(row=row_counter, column=1)


### Lage en funksjon som tar Tkinter input in i funskjonen ###


# ----------------- Run plot --------------------- #

def draw_plot():
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



    global Place, Persons, HomeOffice, Infected, Days, OptionList, opt
    
    # Endrer vi StingVariablene ovenfor
    Place = str(Place.get())
    Persons = int(Persons.get())
    HomeOffice = int(HomeOffice.get())
    Infected = int(Infected.get())
    Days = int(Days.get())
    Density = float(OptionList.get(opt))

    print(type(Place), type(Persons), type(HomeOffice), type(Infected), type(Days), type(Density))

    # Modellparametre
    beta = Density # Kontakt mellom smitte og motakker
    gamma = 1/10 # Tid det tar å bli friskt
    sigma = 0.28 # Antall dager som det tar fra du er smitta til du er smittsom

    # Konstanter
    dt = 0.01 # Endringen av tid
    t_max = Days # Antall dager vi simulerer.
    I_max = []
    N = Persons # Antall Personer

    # Startverdier
    R_0 = 3.53
    I_0 = Infected
    E_0 = I_0 * 10
    S_0 = (Persons - I_0 - R_0 - HomeOffice)
    t_0 = 0
    # Lister for å lagre beregnede verdier,
    # initierer med startverdier
    S_est = [S_0]
    E_est = [E_0]
    I_est = [I_0]
    R_est = [R_0]
    t = [t_0]

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
        

    '''
    Funksjonen som lager hele plotten med matplotlib
    '''

    # plot
    plt.title("Covid-19 Simulation")
    plt.plot(t, S_est, label='Antall Personer')
    plt.plot(t, I_est, label='Antall Smittet')
    plt.plot(t, R_est, label='Antall som har vært smittet')
    plt.xlabel('Dager')
    plt.ylabel('Antall Personer')
    plt.legend()
    plt.grid()

    plt.show()

#    print("Antall: {}, HjemmeKontor: {}, Smittet: {}, Dager: {}, Beta: {}".format(Persons, HomeOffice, Infected, Days, Density))


# Knappen som lager plotten
MakePlot = Tkinter.Button(root, command=draw_plot, text="Create Plot")
MakePlot.pack(side="bottom", fill="both")
root.mainloop()