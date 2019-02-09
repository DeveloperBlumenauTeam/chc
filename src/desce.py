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
import time

if __name__ == '__main__':

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