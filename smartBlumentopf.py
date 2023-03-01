import Tkinter as Tk
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import RPi.GPIO as GPIO
import os

SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)


class GUI(object):
    def __init__(self):
        # Erstellt ein Fenster mit dem Namen Smart Blumentopf, welches unter der Variabel self.root bekannt ist.
        self.root = Tk.Tk()
        self.running = False
        self.root.wm_title("Smart Blumentopf")
        self.root.configure(bg="#137547")

    def run(self):
        # Erstellt ein Feld mit zugehörigem Text. Dieser erklärt das grobe Prinzip des Programms.
        self.ErklaerungsFrame = Tk.Frame(
            self.root, width=500, height=50, bg="#137547")
        self.ErklaerungsFrame.grid(row=0, column=0, columnspan=2)
        self.Erklaerungstext = Tk.Label(self.ErklaerungsFrame, bg="#137547",
                                        text="Wählen Sie zuerst ihre Werte an den Schiebereglern aus. \n Drücken Sie auf starten, wenn Sie fertig sind.", font=14, fg="white")
        self.Erklaerungstext.grid(row=0, column=0)

        # Erstellt ein Feld, und den zugehörigen Text + Button, welche für das Messen und Ausgeben der Feuchtigkeit zuständig sind.
        self.FeuchteFrame = Tk.Frame(
            self.root, width=250, height=120, bg="#137547")
        self.FeuchteFrame.grid(row=1, column=0, padx=10, pady=10)
        self.momFeuchte = Tk.Label(self.FeuchteFrame, bg="#137547",
                                   text="\n Feuchtigkeit bei der letzten Messung:", font=14, fg="white")
        self.momFeuchte.grid(row=0, column=0)
        self.momFeuchteWert = Tk.Label(
            self.FeuchteFrame, bg="#137547", text="0 \n \n", font=14, fg="white")
        self.momFeuchteWert.grid(row=1, column=0)
        self.Messen = Tk.Button(self.FeuchteFrame, text="Jetzt Messen.",
                                bg="#1EBB72", width=25, command=self.messen, font=14)
        self.Messen.grid(row=2, column=0)

        # Erstellt ein Feld, welches nach der Menge an Wasser fragt. Die Eingabe erfolgt per Schieberegler.
        self.MengeFrame = Tk.Frame(
            self.root, width=250, height=120, bg="#137547")
        self.MengeFrame.grid(row=2, column=1, padx=10, pady=10)
        self.Menge = Tk.Label(self.MengeFrame, bg="#137547",
                              text="Menge an Wasser (in ml): \n \n", font=14, fg="white")
        self.Menge.grid(row=0, column=0)
        self.MengeW = Tk.Scale(self.MengeFrame, from_=100, to=1000, resolution=100, length=320,
                               orient="horizontal", font=14, bg="#1EBB72", highlightbackground="#1EBB72")
        self.MengeW.grid(row=1, column=0)

        # Erstellt ein Feld, welches nach dem Rhythmus der Messungen fragt. Die Eingabe erfolgt per Schieberegler.
        self.FeuchteMessenFrame = Tk.Frame(
            self.root, width=250, height=120, bg="#137547")
        self.FeuchteMessenFrame.grid(row=2, column=0, padx=10, pady=10)
        self.FeuchteRhythmus = Tk.Label(self.FeuchteMessenFrame, bg="#137547",
                                        text="Rhythmus der Messungen (in Minuten): \n \n", font=14, fg="white")
        self.FeuchteRhythmus.grid(row=0, column=0, padx=10)
        self.RhythmusInput = Tk.Scale(self.FeuchteMessenFrame, from_=1, to=300, resolution=1,
                                      length=320, orient="horizontal", font=14, bg="#1EBB72", highlightbackground="#1EBB72")
        self.RhythmusInput.grid(row=1, column=0)

        # Erstellt ein Feld, welches die Möglichkeit bietet, die Pflanze zu wässern.
        self.WasserFrame = Tk.Frame(
            self.root, width=250, height=120, bg="#137547")
        self.WasserFrame.grid(row=3, column=0, padx=10, pady=10)
        self.Wasser = Tk.Button(self.WasserFrame, text="Jetzt Waessern.",
                                bg="#1EBB72", width=25, command=self.waessern, font=14)
        self.Wasser.grid(row=0, column=0)

        # Erstellt ein Feld, in dem man wählen kann wie viel Wasser die benutzte Pflanze braucht.
        self.PflanzenFrame = Tk.Frame(
            self.root, width=250, height=120, bg="#137547")
        self.PflanzenFrame.grid(row=1, column=1, padx=10, pady=10)
        self.Art = Tk.Label(self.PflanzenFrame, bg="#137547",
                            text="\n Wie viel Wasser braucht Ihre Pflanze: \n (1 = viel; 2 = mittel; 3 = wenig) \n \n", font=14, fg="white")
        self.Art.grid(row=0, column=0)
        self.PflanzeSlider = Tk.Scale(self.PflanzenFrame, from_=1, to=3, resolution=1, length=320,
                                      orient="horizontal", font=14, bg="#1EBB72", highlightbackground="#1EBB72")
        self.PflanzeSlider.grid(row=1, column=0)

        # Erstellt ein Feld, mit dem man das Programm starten bzw. stoppen kann. Und zusätzlich den Raspberry Pi herunterfahren kann.
        self.SteuerFrame = Tk.Frame(
            self.root, width=250, height=120, bg="#137547")
        self.SteuerFrame.grid(row=3, column=1, padx=10, pady=10)
        self.StartStopp = Tk.Button(self.SteuerFrame, text="Starten",
                                    bg="#1EBB72", width=25, command=self.startstoppen, font=14)
        self.StartStopp.grid(row=0, column=0, pady=5)
        self.Abbruch = Tk.Button(self.SteuerFrame, text="Herunterfahren",
                                 bg="#1EBB72", width=25, command=self.abbruch, font=14)
        self.Abbruch.grid(row=1, column=0, pady=5)

        self.root.mainloop()

    def PumpeAn(self, pin):
        GPIO.output(pin, GPIO.HIGH)

    def PumpeAus(self, pin):
        GPIO.output(pin, GPIO.LOW)

    def messen(self):
        value = 0
        value = mcp.read_adc(1)
        valuegerundet = 100-(value/10.23)
        self.momFeuchteWert.config(text=str(valuegerundet)+"\n")
        return valuegerundet

    def waessern(self):
        self.PumpeAn(3)
        Pumpenzeit = self.wassermenge()
        time.sleep(Pumpenzeit)
        self.PumpeAus(3)

    def abbruch(self):
        os.system("sudo shutdown now")

    def wassermenge(self):
        Menge = self.MengeW.get()
        Pumpenzeit = Menge/200
        return Pumpenzeit

    def messrhythmus(self):
        rhythm = self.RhythmusInput.get()
        minutenrhythm = rhythm / 60
        return minutenrhythm

    def blumentopf(self):
        Pflanzenart = self.Pflanzenwahl()
        rhythm = self.messrhythmus()
        if Pflanzenart == 1:
            self.messen()
            valuegerundet = self.messen()
            if valuegerundet <= 60:
                self.waessern()
        if Pflanzenart == 2:
            self.messen()
            valuegerundet = self.messen()
            if valuegerundet <= 40:
                self.waessern()
        if Pflanzenart == 3:
            self.messen()
            valuegerundet = self.messen()
            if valuegerundet <= 5:
                self.waessern()
        if self.running:
            self.root.after(rhythm, self.blumentopf)

    def startstoppen(self):
        if self.running == True:
            self.StartStopp["text"] = "Starten"
            self.running = False
        else:
            self.StartStopp["text"] = "Stoppen"
            self.running = True
            self.blumentopf()

    def Pflanzenwahl(self):
        Pflanzenart = self.PflanzeSlider.get()
        return Pflanzenart


GUI().run()
