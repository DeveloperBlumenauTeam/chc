#!/usr/bin/env python3
'''
Created on 20190216
Update on 20190216
@author: Marco Aurelio
'''

#pylint: disable=C0301
#pylint: disable=C0103
#pylint: disable=W0703
#pylint: disable=R0913

import RPi.GPIO as gpio
import time
import logging
import os
from Pipe import Pipe
from GracefulKiller import GracefulKiller

def setup():
    gpio.setwarnings(False)
    #Configuring GPIO
    gpio.setmode(gpio.BOARD)
    gpio.setup(32, gpio.OUT)

    #Configura saída PWM no pino 32 e frequênci de 100Hz - AJUSTAR A FREQUENCIA
    rotacao = gpio.PWM(32, 100)
    rotacao.start(0)

    return rotacao

if __name__ == '__main__':
    '''
    [Entry point do programa]
    '''
    # controle de crt-c
    kill = GracefulKiller()

    # ajusta o log
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    logging.info('Inicio...')
    
    # define o pipe
    pipe_path = '/tmp/velocidade.pipe'

    # configura hardware
    rot = setup()

    # abre o calar do pipe como leitura sem bloqueio
    servidor = Pipe(pipe_path)
    servidor.open(os.O_RDONLY | os.O_NONBLOCK)

    logging.info('Descritor Servidor Aberto')

    while kill.kill_now is False:
        # le o pipe
        val = servidor.readLine(timeout=10)
        if val is not None: #se None nao veio nada
            try:
                # valor se numerico inteiro
                velocidade = int(val)
            except:
                logging.error('Falha valor fora da faixa: %s',str(val))
                continue

            # valida range 0-100
            if 0 <= velocidade <= 100:
                logging.info('Nova Velocidade:%d',velocidade)
                rot.start(velocidade)
            else:
                logging.error('Velocidade fora de faixa:%d', velocidade)
    
    # crt-c detectado enceramento de app
    logging.info('App Sinalizado para fechamento')
