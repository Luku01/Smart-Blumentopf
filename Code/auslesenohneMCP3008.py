import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD) # Setzt die Art wie die Pins gezählt werden
GPIO.setup(40, GPIO.IN) # Setzt den 40ten Pin als Input fest
if GPIO.input(40) == GPIO.LOW: # Wenn der Pin als Input eine 1 bzw.…
	print(“Es ist feucht.”) # …high bekommt, wird dies ausgegeben
else:
	print(“Es ist nicht feucht.”) # Wenn nicht, wird dies ausgegeben
