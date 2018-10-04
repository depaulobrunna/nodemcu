import esp
import machine
#from machine import Pin, PWM
import time

def main():
    servo = machine.PWM(machine.Pin(5), freq=50)
    print('something')
    '''p5 = machine.Pin(5)
    pwm5 = machine.PWM(p5)
    pwm5.freq(50)
    pwm5.duty(25)
    while(True):
        #servo.duty(44)'''
    while(True):
        servo.duty(58)
        time.sleep_ms(3000)
        servo.duty(100)
        time.sleep_ms(3000)
        #servo.duty(77)
        #time.sleep_ms(500)

if __name__ == '__main__':
    print("main entered")
    main()