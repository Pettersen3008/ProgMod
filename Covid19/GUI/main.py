'''

Laget av Sander Pettersen

Kilder: {

https://docs.python.org/3/library/tkinter.html
}

'''
from tkinter import Frame, OptionMenu, Label, Button, Entry, Grid
import tkinter as tk
import matplotlib.pyplot as plt

root = tk.Tk()

# Title
root.title('Covid 19 Simulation')

# Setter background, (må sette bg på hver Frame)
# root.config(bg="white")

# Størrelse på skjermen
root.width = 600
root.height = 900
root.geometry('{}x{}'.format(root.width, root.height))



class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master
        self.pack()

        # Div for Heading
        self.heading = Frame(root)
        self.heading.pack(side="top", pady=100)

        # Div for hver info_var
        self.frame = Frame(root)
        self.frame.pack(side="top", pady=50)

        # Div for "Fortsett eller Avslutt"
        self.bottom = Frame(root)
        self.bottom.pack(side="bottom", pady=60)

        # Kjører funkjsonen under
        self.create_gui()

    def create_gui(self, *args):
        '''
        Lagrer alt av informasjon som trengs til å plotte
        '''

        heading = Label(self.heading, text="Covid 19 Sim", font="Helvetica 32")
        heading.pack(side="top")

        row_counter = 0

        # Place
        self.place = tk.StringVar()
        self.place.set('Skien')

        # Persons 
        self.persons = tk.IntVar()
        self.persons.set(1100)

        # Homeoffice
        self.home = tk.IntVar()
        self.home.set(3)

        # Infected
        self.infected = tk.IntVar()
        self.infected.set(5)

        # Days 
        self.days = tk.IntVar()
        self.days.set(100)

        # Beta Option
        optionList = { 'Lite' : 0.25, 'Medium' : 0.37, 'Stor' : 0.50 }

        for opt in optionList:
            print(optionList[opt])
        
        self.option = tk.StringVar()
        self.option.set(opt)

        label = Label(self.frame, text="Hvor høy smitte rate har dere : ")
        label.grid(row=5, column=0, pady=20)
        entry = OptionMenu(self.frame, self.option, *optionList)
        entry.grid(row=5, column=1)


        # Lager en ordbok med quoats jeg vil ha med og lister de.
        textDict = {"Hvilken område vil du simulere : " : 0 , "Hvor mange er dere på dette område : " : 1, "Hvor mange holder seg hjemme : " : 2, "Hvor mange er allerede smittet : " : 3, "Hvor mange dager vil du simulere : " : 4}
        self.textList = list(textDict)
        
        # Samme med disse bare lager en liste direkte
        self.infoList = [self.place, self.persons, self.home, self.infected, self.days]

        # Lager en for loop istedet for å kopiere alt så koden blir litt mindre

        # PS !!! TIPS fra alex forrige time

        for alt in range(len(self.textList)):
            label = Label(self.frame, text=self.textList[alt])
            label.grid(row=row_counter, column=0, pady=20)
            entry = Entry(self.frame, textvariable=self.infoList[alt], width=8)
            entry.grid(row=row_counter, column=1)
            row_counter += 1

        # ShortKeys for å gå vidre eller avslutte program
        self.master.bind('<Return>', self.draw_plot)
        self.master.bind('<Escape>', quit)

        # Button for å avslutte program
        self.quit = Button(self.bottom, text="Avslutt", fg="black", command=self.master.destroy)
        self.quit.pack(side="bottom")

        # Infomasjon
        self.text = Label(self.bottom, text="For å fortsette trykk ENTER ! \n Hvis du vil avslutte trykk ESC")
        self.text.pack(side="bottom")
        
    def covid(self):
        # Modellparametre
        beta = 0.25 # Kontakt mellom smitte og motakker
        gamma = 1/10 # Tid det tar å bli friskt
        dt = 0.01 # Endringen av tid
        t_max = self.days.get() # Antall dager vi simulerer.
        N = self.persons.get() # Antall Personer

        # Startverdier
        R_0 = (beta/gamma)
        I_0 = self.infected.get()
        S_0 = (N - I_0 - R_0)
        t_0 = 0

        # Lister for å lagre beregnede verdier,
        # initierer med startverdier
        self.S_est = [S_0]
        self.I_est = [I_0]
        self.R_est = [R_0]
        self.t = [t_0]

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
        while self.t[-1] < t_max:
            # Regn ut neste S
            S_deriv = dSdt(self.S_est[-1], self.I_est[-1])
            self.S_est.append(euler(self.S_est[-1], S_deriv, dt))

            # Regn ut neste I
            I_deriv = dIdt(self.S_est[-1], self.I_est[-1])
            self.I_est.append(euler(self.I_est[-1], I_deriv, dt))

            # Regn ut neste R
            R_deriv = dRdt(self.I_est[-1])
            self.R_est.append(euler(self.R_est[-1], R_deriv, dt))

            # Lagre tid og legge til endringen av tid
            self.t.append(self.t[-1] + dt)

    def draw_plot(self, *args, **kwargs):
        '''
        Funksjonen som lager hele plotten med matplotlib
        '''
        self.covid() # kjører korona funksjonen
        # plot
        plt.title("Covid-19 Simulation of {}".format(self.place.get()))
        plt.plot(self.t, self.S_est, label='Antall Personer')
        plt.plot(self.t, self.I_est, label='Antall Smittet')
        plt.plot(self.t, self.R_est, label='Antall som har vært smittet')
        plt.xlabel('Dager')
        plt.ylabel('Antall Personer')
        plt.legend()
        plt.grid()

        plt.show()


# Kjører class App tk.root
covid = App(root)

# Kjører tk.mainloop
covid.mainloop()
