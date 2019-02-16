def velocidade(velo):
    #A velocidade deve estar entre 0 e 100
    #Define Libraries  
    import RPi.GPIO as gpio
    import time
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
#End code desativado para que não desligue o PWM
#gpio.cleanup() - #não sei se tem que deixar a função exit() abaixo
#exit()
