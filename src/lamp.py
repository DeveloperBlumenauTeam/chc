#!/usr/bin/env python3
'''
Created on 20190209
Update on 20190209
@author: Marco Aurelio
'''

#pylint: disable=C0301
#pylint: disable=C0103
#pylint: disable=W0703
#pylint: disable=R0913

import RPi.GPIO as gpio


if __name__ == '__main__':

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
    