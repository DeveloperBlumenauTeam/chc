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
  
import RPi.GPIO as gpio
import time

import argparse

def velocidade(velo):
    '''[Ajusta velocidade]
    Arguments:
        velo {[int]} -- [deve estar entre 0 e 100]
    '''
    #Configuring don’t show warnings
    gpio.setwarnings(False)

    #Configuring GPIO
    gpio.setmode(gpio.BOARD)
    gpio.setup(32,gpio.OUT)

    #Configura saída PWM no pino 32 e frequênci de 100Hz - AJUSTAR A FREQUENCIA
    rotacao = gpio.PWM(32,100)
    #rotacao.start(0) #Não inicia a rotação com 0, mas com o valor "velo"

    #copia a velocidade para a porta
    rotacao.start(velo)

if __name__ == '__main__':
    '''
    [Entry point do programa]
    '''

    # configura argumentos e descereve da aplicacao 
    parser_val = argparse.ArgumentParser(description='Altera velocidade rotacao')
    
    # define que -v é argumento obrigatorio e com valor
    parser_val.add_argument('-v', '--velocidade', help='ajuste nova velocidade', required=True)

    # execurta o parse validando itens acima, gera erro se argumentos obrigatorios não forem passados 
    args = parser_val.parse_args()

    # pega valor da velocidade definida na linha 44
    vel = int(args.velocidade)

    # chama a função passando parametro vel
    velocidade(vel)
    
    # exibe mensagem na saida
    print('Velocidade ajustada para:{0}'.format(vel))

    