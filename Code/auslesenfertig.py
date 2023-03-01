# -*- coding: iso-8859-1 -*-
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.Mcp3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Lässt den Benutzer wählen wie viel Feuchtigkeit seine Pflanze braucht.
plant = raw_input(
    "Um welche Pflanze handelt es sich? A: Braucht viel Feuchtigkeit; B: Braucht mäßige Feuchtigkeit; C: Braucht kaum Feuchtigkeit")
if plant == "A" or plant == "a":
    rhythm = input(
        "In welchem Rhythmus sollen die Werte ausgelesen werden?(Sekunden)")
    print(" ")
    print("Lese die Feuchtigkeitswerte aus. Drücke Str-C zum Beenden.")
    print(" ")
    print("|Feuchtigkeit| |Status|")
    print("-" * 23)
    while True:
        value = mcp.read_adc(1)
        valueberechnet = 100-value/10.23
        output = "| {0:<12.3f} | |{1:<7}|"
        # Wenn die Werte die bestimmten Bereiche überschreiten, werden der Messwert + Hilfswort ausgegeben
        if valueberechnet > 80.00:
            print(output.format(valueberechnet, "Feucht"))
        if valueberechnet < 80.00 and valueberechnet > 60.00:
            print(output.format(valueberechnet, "Mittel"))
        if valueberechnet < 60.00:
            print(output.format(valueberechnet, "Trocken"))
        time.sleep(rhythm)
if plant == "B" or plant == "b":
    rhythm = input(
        "In welchem Rhythmus sollen die Werte ausgelesen werden?(Sekunden)")
    print(" ")
    print("Lese die Feuchtigkeitswerte aus. Drücke Str-C zum Beenden.")
    print(" ")
    print("|Feuchtigkeit| |Status|")
    print("-" * 23)
    while True:
        value = mcp.read_adc(1)
        valueberechnet = 100-value/10.23
        output = "| {0:<12.3f} | |{1:<7}|"
        # Wenn die Werte die bestimmten Bereiche überschreiten, werden der Messwert + Hilfswort ausgegeben
        if valueberechnet > 60.00:
            print(output.format(valueberechnet, "Feucht"))
        if valueberechnet < 60.00 and valueberechnet > 40.00:
            print(output.format(valueberechnet, "Mittel"))
        if valueberechnet < 40.00:
            print(output.format(valueberechnet, "Trocken"))
        time.sleep(rhythm)
if plant == "C" or plant == "c":
    rhythm = input(
        "In welchem Rhythmus sollen die Werte ausgelesen werden?(Sekunden)")
    print(" ")
    print("Lese die Feuchtigkeitswerte aus. Drücke Str-C zum Beenden.")
    print(" ")
    print("|Feuchtigkeit| |Status|")
    print("-" * 23)
    while True:
        value = mcp.read_adc(1)
        valueberechnet = 100-value/10.23
        output = "| {0:<12.3f} | |{1:<7}|"
        # Wenn die Werte die bestimmten Bereiche überschreiten, werden der Messwert + Hilfswort ausgegeben
        if valueberechnet > 35.00:
            print(output.format(valueberechnet, "Feucht"))
        if valueberechnet < 35.00 and valueberechnet > 15.00:
            print(output.format(valueberechnet, "Mittel"))
        if valueberechnet < 5.00:
            print(output.format(valueberechnet, "Trocken"))
        time.sleep(rhythm)
