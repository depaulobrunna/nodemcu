import esp
import machine
from machine import Pin, PWM
import time

def pwm_motor(freq, duty):
    pwm_dc = PWM(Pin(5))
    pwm_dc.freq(freq)
    pwm_dc.duty(duty)

def pwm_servo(duty_cycle):
    #save_duty = pwm_dc.duty()
    #save_freq = pwm_dc.freq()
    pwm_servo = machine.PWM(machine.Pin(0), freq=50)
    pwm_servo.duty(duty_cycle)
    time.sleep_ms(500)
    pwm_servo.deinit()
    #pwm_motor(save_freq, save_duty)
    

def main():
    print('main')
    in3 = Pin(16, Pin.OUT)
    in4 = Pin(4, Pin.OUT)
    while(True):
        pwm_motor(1000, 200)
        time.sleep(1)
        pwm_servo(60)
        time.sleep(1)
        pwm_servo(100)
        time.sleep(1)
main()