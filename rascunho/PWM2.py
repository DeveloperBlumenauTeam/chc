#Define Libraries  --  Programa escrito em Python 2
import RPi.GPIO as gpio
import time

#Configuring GPIO 
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(11,gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(12,gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(40,gpio.OUT)

#Configuring GPIO as PWM
pwm = gpio.PWM(40,100)

#Initializing PWM
pwm.start(50)
dc = 50
print("Duty Cycle:",dc)
pwm.ChangeDutyCycle(dc) 

#Defining the detection in rising edge
gpio.add_event_detect(11,gpio.RISING,bouncetime = 300)
gpio.add_event_detect(12,gpio.RISING,bouncetime = 300)

while True:
        
    # Increasing the duty cycle of the PWM waveform
    if gpio.event_detected(11):
        dc = dc + 10
        if dc == 110:
            dc = 0
        print("Duty Cycle:",dc)        
        pwm.ChangeDutyCycle(dc)
        
    # Decreasing the duty cycle of the PWM waveform     
    elif gpio.event_detected(12):
        dc = dc - 10
        if dc == -10:
            dc = 100
        print("Duty Cycle:",dc)        
        pwm.ChangeDutyCycle(dc)         
    
    time.sleep(0.1)

gpio.cleanup()
exit()