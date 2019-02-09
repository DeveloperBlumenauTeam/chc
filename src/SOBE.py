import RPi.GPIO as gpio 
import time
#configurando como BOARD, indentificação física dos pinos
gpio.setmode(gpio.BOARD)
#pino 20 configurado como saída
gpio.setup(20, gpio.OUT)
#ativa o rele SOBE
gpio.outpot(20, gpio.HIGH)
#agurada 0,5 segundos - deve ser ajustado
time.sleep(0,5)
#desativa o rele SOBE
gpio.output(20, gpio.LOW)
#desfaz os ajustes do GPIO - não sei porque
gpio.cleanup()