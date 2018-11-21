import esp
import machine
from machine import Pin, PWM
import time

class pwm_control:
    
    def __init__(self, name, dc_pin, srv_pin):
        pwm_dc = PWM(dc_pin)
        pwm_servo = machine.PWM(machine.Pin(srv_pin), freq=50)
        
    def pwm_motor(duty):
        pwm_dc.freq(1000)
        pwm_dc.duty(duty)
        
    def pwm_servo(duty):
        pwm_servo.duty(duty)
        time.sleep_ms(500)
        pwm_servo.deinit()

    