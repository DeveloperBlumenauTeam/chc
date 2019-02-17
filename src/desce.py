#!/usr/bin/env python3
'''
Created on 20190209
Update on 20190217
@author: Marco Aurelio
'''

#pylint: disable=C0301
#pylint: disable=C0103
#pylint: disable=W0703
#pylint: disable=R0913

import RPi.GPIO as gpio 
import time

if __name__ == '__main__':

    # desativa os alarmes
    gpio.setwarnings(False)
    #configurando como BOARD, indentificação física dos pinos
    gpio.setmode(gpio.BOARD)
    #pino 36 configurado como saída
    gpio.setup(36, gpio.OUT)
    #pino 26 configurado com entrada - Fim de Curso Desce
    gpio.setup(26, gpio.IN)
    #ativa o rele DESCE
    gpio.output(36, gpio.HIGH)
    #agurada 0,5 segundos - deve ser ajustado
    time.sleep(0.5)
    #desativa o rele DESCE
    gpio.output(36, gpio.LOW)
    #desfaz os ajustes do GPIO - não sei porque
    #gpio.cleanup()
    #testa se o fim de curso foi acionado
    val = gpio.input(26)
    print(val)
    # 0 - fim de curso acionado
    # 1 - fim de curso "Não" acionado
