import esp
import machine
from machine import I2C
import time

def main():
    servo = machine.PWM(machine.Pin(5), freq=50)
    while(True):
        servo.duty(60)
        time.sleep_ms(500)
        servo.duty(100)
        time.sleep_ms(500)
        
main()