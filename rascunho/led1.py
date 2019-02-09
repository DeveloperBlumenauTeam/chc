#Programa escrito em Python 2

import RPi.GPIO as gpio
import time

# Configurando como BOARD, Pinos Fisicos
gpio.setmode(gpio.BOARD)

# Configurando a direcao do Pino
gpio.setup(11, gpio.OUT) # Usei 11 pois meu setmode é BOARD, se estive usando BCM seria 17
while True:
    gpio.output(11, gpio.HIGH)
    time.sleep(2)
    gpio.output(11, gpio.LOW)
    time.sleep(2)

# Desfazendo as modificações do GPIO
gpio.cleanup()