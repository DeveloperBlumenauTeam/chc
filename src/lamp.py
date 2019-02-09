import RPi.GPIO as gpio
# desativa os alarmes
gpio.setwarnings(False)
#configura como BOARD, identificação física dos pinos
gpio.setmode(gpio.BOARD)
#pino 12 configurado como saída para a lâmpada
lamp = gpio.input(12)
if lamp:
    #se lamp = 1 desliga
    gpio.output(12, gpio.LOW)
else:
    #se lamp = 0 liga
    gpio.output(12, gpio.HIGH)
    