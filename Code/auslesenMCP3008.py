import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
SPI_PORT = 0  # Sagt dem Raspberry Pi an welcher Stelle der…
SPI_DEVICE = 0  # …MCP3008 angeschlossen ist
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
while True:  # Endlos-Schleife
    value = 0
    value = mcp.read_adc(0)  # Liest den MCP3008 aus.
    print(value)  # Gibt den Messwert aus.
    time.sleep(1)  # Jede Sekunde wird die Schleife durchlaufen. 
# Dieser Wert ist frei wählbar und kann je nach Situation angepasst werden.
