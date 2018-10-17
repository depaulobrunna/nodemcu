import esp
import machine
import time

def main():
    print('main')
    i2c = machine.I2C(scl=machine.Pin(14), sda=machine.Pin(2))
    while(True):
        addr = i2c.scan()
        reg = 0x00
        while(reg < 118):
            print('reg:', reg, i2c.readfrom_mem(addr[0], reg, 2))
            time.sleep_ms(500)
            reg = reg + 1
main()
