import RPi.GPIO as gpio 
import time
#configurando como BOARD, indentificação física dos pinos
gpio.setmode(gpio.BOARD)
#pino 16 configurado como saída
gpio.setup(16, gpio.OUT)
#ativa o rele DESCE
gpio.outpot(16, gpio.HIGH)
#agurada 0,5 segundos - deve ser ajustado
time.sleep(0,5)
#desativa o rele DESCE
gpio.output(16, gpio.LOW)
#desfaz os ajustes do GPIO - não sei porque
gpio.cleanup()