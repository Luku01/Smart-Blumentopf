# -*- coding: iso-8859-1 -*-
import tkinter as Tk


class GUI(object):
    def __init__(self):
        # Erstellt ein Fenster mit dem Namen Smart Blumentopf, welches unter der Variabel self.root bekannt ist.
        self.root = Tk.Tk()
        # Das Fenster bekommt den Titel Smart Blumentopf.
        self.root.wm_title("Smart Blumentopf")
        # Zusätzlich bekommt es noch grün als Hintergrundfarbe…
        self.root.configure(bg="#137547")
        # …und die Bildschirm-Maße des Raspberry-Pis.
        self.root.geometry("800x440")

    def run(self):
        # Erstellt ein Frame in der 1. Reihe und über 2 Spalten
        self.ErklaerungsFrame = Tk.Frame(
            self.root, width=500, height=50, bg="#137547")
        self.ErklaerungsFrame.grid(row=0, column=0, columnspan=2, padx=25)
        # Erstellt ein Label mit Text
        self.Erklaerungstext = Tk.Label(self.ErklaerungsFrame, bg="#137547",
                                        text="Wählen Sie zuerst ihre Werte an den Schiebereglern aus. \n Drücken Sie auf Starten, wenn Sie fertig sind.",
                                        font=14, fg="white")
        self.Erklaerungstext.grid(row=0, column=0)

        # Erstellt ein Frame in der 2. Reihe und der 1. Spalte
        self.FeuchteFrame = Tk.Frame(
            self.root, width=250, height=120, bg="#137547")
        self.FeuchteFrame.grid(row=1, column=0, padx=35, pady=10)
        # Erstellt ein Label mit Text
        self.momFeuchte = Tk.Label(self.FeuchteFrame, bg="#137547",
                                   text="\n Feuchtigkeit bei der letzten Messung:", font=14, fg="white")
        self.momFeuchte.grid(row=0, column=0)
        # Erstellt ein weiteres Label was durch die Messwerte ersetzt werden soll
        self.momFeuchteWert = Tk.Label(
            self.FeuchteFrame, bg="#137547", text="0 \n \n", font=14, fg="white")
        self.momFeuchteWert.grid(row=1, column=0)
        # Erstellt ein Knopf mit dem man direkt messen kann
        self.Messen = Tk.Button(self.FeuchteFrame, text="Jetzt Messen.",
                                bg="#1EBB72", width=25, command=self.messen, font=14)
        self.Messen.grid(row=2, column=0)

        # Erstellt ein Frame in der 2. Reihe  und der 2. Spalte
        self.PflanzenFrame = Tk.Frame(
            self.root, width=250, height=120, bg="#137547")
        self.PflanzenFrame.grid(row=1, column=1, padx=35, pady=10)
        # Erstellt ein Label mit Text
        self.Art = Tk.Label(self.PflanzenFrame, bg="#137547",
                            text="\n Wie viel Wasser braucht Ihre Pflanze: \n (1 = viel; 2 = mittel; 3 = wenig) \n \n", font=14, fg="white")
        self.Art.grid(row=0, column=0)
        # Erstellt einen Scheiberegler mit dem man seine Pflanzenart wählen kann
        self.PflanzeSlider = Tk.Scale(self.PflanzenFrame, from_=1, to=3, resolution=1, length=320,
                                      orient="horizontal", font=14, bg="#1EBB72", highlightbackground="#1EBB72")
        self.PflanzeSlider.grid(row=1, column=0)

        # Erstellt ein Feld in der 3. Reihe und der 1. Spalte
        self.FeuchteMessenFrame = Tk.Frame(
            self.root, width=250, height=120, bg="#137547")
        self.FeuchteMessenFrame.grid(row=2, column=0, padx=35, pady=10)
        # Erstellt ein Label mit Text
        self.FeuchteRhythmus = Tk.Label(self.FeuchteMessenFrame, bg="#137547",
                                        text="Rhythmus der Messungen (in Minuten): \n", font=14, fg="white")
        self.FeuchteRhythmus.grid(row=0, column=0, padx=10)
        # Erstellt ein Schieberegler mit dem man den Rhytmus wählen kann, mit dem die Schleife durchlaufen wird
        self.RhythmusInput = Tk.Scale(self.FeuchteMessenFrame, from_=1, to=300, resolution=1,
                                      length=320, orient="horizontal", font=14, bg="#1EBB72", highlightbackground="#1EBB72")
        self.RhythmusInput.grid(row=1, column=0)

        # Erstellt ein Frame in der 3.Reihe und der 2. Spalte
        self.MengeFrame = Tk.Frame(
            self.root, width=250, height=120, bg="#137547")
        self.MengeFrame.grid(row=2, column=1, padx=35, pady=10)
        # Erstellt ein Label mit Text
        self.Menge = Tk.Label(self.MengeFrame, bg="#137547",
                              text="Menge an Wasser (in ml): \n", font=14, fg="white")
        self.Menge.grid(row=0, column=0)
        # Erstellt ein Schieberegler, an welchem man die Menge an Wasser wählen kann
        self.MengeW = Tk.Scale(self.MengeFrame, from_=100, to=1000, resolution=100, length=320,
                               orient="horizontal", font=14, bg="#1EBB72", highlightbackground="#1EBB72")
        self.MengeW.grid(row=1, column=0)

        # Erstellt ein Frame in der 4. Reihe und 1. Spalte
        self.WasserFrame = Tk.Frame(
            self.root, width=250, height=120, bg="#137547")
        self.WasserFrame.grid(row=3, column=0, padx=35, pady=10)
        # Erstellt einen Knopf, mit dem man die Pflanze wässern kann
        self.Wasser = Tk.Button(self.WasserFrame, text="Jetzt Waessern.",
                                bg="#1EBB72", width=25, command=self.waessern, font=14)
        self.Wasser.grid(row=0, column=0)

        # Erstellt ein Frame in der 4. Reihe und der 2. Spalte
        self.SteuerFrame = Tk.Frame(
            self.root, width=250, height=120, bg="#137547")
        self.SteuerFrame.grid(row=3, column=1, padx=35, pady=10)
        # Erstellt einen Knopf, mit dem man die Schleife starten kann
        self.StartStopp = Tk.Button(self.SteuerFrame, text="Starten",
                                    bg="#1EBB72", width=25, command=self.startstoppen, font=14)
        self.StartStopp.grid(row=0, column=0, pady=5)
        # Erstellt einen Knopf, mit dem man den Raspberry Pi herunterfahren kann
        self.Abbruch = Tk.Button(self.SteuerFrame, text="Herunterfahren",
                                 bg="#1EBB72", width=25, command=self.abbruch, font=14)
        self.Abbruch.grid(row=1, column=0, pady=5)

        # Die Schleife des Fensters
        self.root.mainloop()

    def messen(self):
        pass

    def waessern(self):
        pass

    def abbruch(self):
        pass

    def wassermenge(self):
        pass

    def messrhythmus(self):
        pass

    def blumentopf(self):
        pass

    def startstoppen(self):
        pass

    def Pflanzenwahl(self):
        pass


# Erstellt alle Frames, Labels und Knöpfe
GUI().run()
