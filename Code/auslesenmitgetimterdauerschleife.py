import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.Mcp3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Fragt nach in welchem Rhythmus die Schleife durchlaufen werden soll.
rhythm = input("In welchem Rhythmus sollen die Werte ausgelesen werden?(Sekunden)")
print(" ")   # Erzeugt eine leere Zeile -> Übersichtlichkeit
print("Lese die Feuchtigkeitswerte aus. Drücke Str-C zum Beenden.")
print(" ")
print("| Feuchtigkeit |")  # Überschrift einer Tabelle
print("-" * 14)  # Erzeugt eine Linie
while True:
    value = mcp.read_adc(1)
    valueberechnet = 100-value/10.23
    output = ("| {0: < 10.3f} |")
    # Gibt die Werte in Form einer Tabelle wieder aus
    print(output.format(valueberechnet))
    time.sleep(rhythm)
