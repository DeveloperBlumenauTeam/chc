#!/usr/bin/env python3
'''
Created on 20161125
Update on 20180105
@author: Eduardo Pagotto
'''
#pylint: disable=C0301
#pylint: disable=C0103
#pylint: disable=W0703

import os
import errno
import time
import logging

from GracefulKiller import GracefulKiller

BUFFER_SIZE = 65536

class Pipe(object):
    '''Wrapper PIPE Fifo'''

    def __init__(self, path):
        '''Cria ou vincula o Pipe'''
        self.path = path
        self.io = None
        self.is_open = False
        self.kill = GracefulKiller()


        if not os.path.exists(self.path):
            try:
                os.mkfifo(self.path)
                logging.info('Pipe %s criado', self.path)
            except FileExistsError:
                logging.warning('Pipe %s vinculado', self.path)
            except Exception as ex:
                logging.exception('Falha grave ao vincular Pipe:%s Erro:%s', self.path, ex)
        else:
            logging.warning('Pipe %s vinculado', self.path)

    def __del__(self):
        self.close()

    def open(self, flags_op):#os.O_RDONLY | os.O_NONBLOCK ( os.O_WRONLY )
        '''Abre Fifo como leitura sem Bloquear'''
        self.io = os.open(self.path, flags_op)
        self.is_open = True
        logging.info('Pipe %s aberto como %d', self.path, flags_op)

    def close(self):
        '''Encerra uso do fifo'''
        if self.is_open is True:
            os.close(self.io)
            logging.info('Pipe %s fechado', self.path)
            self.is_open = False

    def read(self):
        '''Le dados do pipe'''
        try:
            return os.read(self.io, BUFFER_SIZE)

        except OSError as err:
            if err.errno == errno.EAGAIN or err.errno == errno.EWOULDBLOCK:
                return None
            else:
                raise err

    def readLine(self, timeout=1):
        '''Le linha no pipe'''

        contador_vazio = 0
        while True:

            if self.kill.kill_now is True:
                return None

            array_bytes_in = self.read()
            if len(array_bytes_in) == 0:
                    contador_vazio += 1
                    if contador_vazio > timeout * 2:
                        return None
                    time.sleep(0.5)
                    continue
            else:
                break

        saida = array_bytes_in.decode('UTF-8').replace('\n','')
        return saida

    def write(self, buffer_texto):
        '''Escre no pipe aberto'''
        buffer = buffer_texto.encode(encoding='UTF-8')
        os.write(self.io, buffer)

