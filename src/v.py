#!/usr/bin/env python3
'''
Created on 20190209
Update on 20190216
@author: Marco Aurelio
'''

#pylint: disable=C0301
#pylint: disable=C0103
#pylint: disable=W0703
#pylint: disable=R0913
  
#import RPi.GPIO as gpio
import time

import argparse

def velocidade(velo):
    '''[Ajusta velocidade]
    Arguments:
        velo {[int]} -- [deve estar entre 0 e 100]
    '''
    pass
    # #Configuring don’t show warnings
    # gpio.setwarnings(False)

    # #Configuring GPIO
    # gpio.setmode(gpio.BOARD)
    # gpio.setup(32,gpio.OUT)

    # #Configura saída PWM no pino 32 e frequênci de 100Hz - AJUSTAR A FREQUENCIA
    # rotacao = gpio.PWM(32,100)
    # #rotacao.start(0) #Não inicia a rotação com 0, mas com o valor "velo"

    # #copia a velocidade para a porta
    # rotacao.start(velo)

if __name__ == '__main__':

    #configura argumentos e help da aplicacao 
    parser_val = argparse.ArgumentParser(description='Altera velocidade')
    parser_val.add_argument('-v',
                            '--velocidade',
                            help='ajuste nova velocidade',
                            required=True)

    args = parser_val.parse_args()

    vel = int(args.velocidade)


    velocidade(vel)
    
    
    print('Velocidade austada para:{0}'.format(vel))

    