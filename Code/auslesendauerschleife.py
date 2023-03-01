import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
SPI_PORT = 0		
SPI_DEVICE = 0		
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
while True:			 
	value = 0			
	value = mcp.read_adc(0)	
	#Teilt den Wert, um auf Werte zwischen 0 und 100 zu kommen.
	#Danach wird der Wert gedreht und gerundet.
	print(format((100-value/10,23), ".3f"))	
	time.sleep(1)			
