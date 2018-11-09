import esp
import machine
from machine import Pin, PWM
import time

def pwm_motor(duty):
    pwm_dc = PWM(Pin(5))
    pwm_dc.freq(1000)
    pwm_dc.duty(duty)

def pwm_servo(duty_cycle):
    pwm_servo = machine.PWM(machine.Pin(0), freq=50)
    pwm_servo.duty(duty_cycle)
    time.sleep_ms(500)
    #add func para desligar o pino do servo

def main():
    print('main')
    in3 = Pin(16, Pin.OUT)
    in4 = Pin(4, Pin.OUT)
    while(True):
        pwm_motor(200)
        time.sleep(1)
        pwm_servo(60)
        time.sleep(1)
        pwm_servo(100)
        time.sleep(1)
main()