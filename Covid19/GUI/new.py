import tkinter as Tkinter
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt

# Define a bold font:
BOLD = ('Courier', '24', 'bold')
# ----------------- Main of GUI --------------------- #

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

OptionList = [
    "Lite",
    "Medium",
    "Stor"
]

OptionList[0] = float(0.25)
OptionList[1] = float(0.37)
OptionList[2] = float(0.50)

Density = Tkinter.StringVar()
Density.set(OptionList[1])

Option = Tkinter.OptionMenu(root, Density, *OptionList)
Option.config(width=8)
Option.pack(side="top")

# ----------------- Create row values --------------------- #
# Create text boxes and entry boxes for the variables.
# Use grid geometry manager instead of packing the entries in.
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

# ----------------- Run plot --------------------- #

def draw_plot():

    global Place, Persons, HomeOffice, Infected, Days, Density

    # Endrer vi StingVariablene ovenfor

    # String har ingen get verdi
#    Place = str(Place.get())

    # Alle int ble float pga float har get verdi
    Persons = int(Persons.get())
    HomeOffice = int(HomeOffice.get())
    Infected = int(Infected.get())
    Days = int(Days.get())
    Density = float(Density.get())

    t = 100

    # plot
    plt.figure()
    plt.title("Covid-19 Simulation")
    plt.plot(t, Density, label='Antall Personer')
#    plt.plot(t, Persons, label='Antall Smittet')
#    plt.plot(t, HomeOffice, label='Antall som har vært smittet')
    plt.xlabel('Dager')
    plt.ylabel('Antall Personer')
#    plt.legend()
    plt.grid()

    plt.show()



    ## Test
        # Define the range of the plot.
    t_min = -10
    t_max = 10
    dt = 0.01
    t = np.arange(t_min, t_max+dt, dt)

# Knappen som kjører plotten
MakePlot = Tkinter.Button(root, command=draw_plot, text="Create Plot")
MakePlot.pack(side="bottom", fill="both")

# Kjører vinduet
root.mainloop()


#   if __name__ == "__main__":
#   Kjører tkinter vinduet
