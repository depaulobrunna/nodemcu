import esp
import machine
import time

def main():
    print('main')
    i2c = machine.I2C(scl=machine.Pin(14), sda=machine.Pin(2))
    while(True):
        time.sleep(1)
        print('barramento:', i2c.scan())
        
main()