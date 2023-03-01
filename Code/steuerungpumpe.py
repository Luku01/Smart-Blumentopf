import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)


def PumpeAn(pin):
    # Schaltet die Pumpe an, indem der Pin auf high gesetzt wird
    GPIO.output(pin, GPIO.HIGH)


def PumpeAus(pin):
    # Schaltet die Pumpe aus, indem der Pin auf low gesetzt wird
    GPIO.output(pin, GPIO.LOW)


PumpeAn(3)  # Schaltet die Pumpe an…
PumpeAus(3)  # …und schaltet die Pumpe wieder aus
