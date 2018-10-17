import esp
import machine
import time

def main():
    print('main')
    i2c = machine.I2C(scl=machine.Pin(14), sda=machine.Pin(2))
    while(True):
        addr = i2c.scan()
        print('i2c device address:', addr[0])
        time.sleep(1)
        if(addr[0] == (int)(0x68)):
            print('MPU6050 device found!!!')
        time.sleep(1)
        reg = 0x6B
        data = (i2c.readfrom_mem(addr[0], reg, 1))
        if(data[0] == (int)(0x40)):
            print('reg:', reg, 'pwr:',(data))
        time.sleep(1)
        reg = 0x75
        data = i2c.readfrom_mem(addr[0], reg, 1)
        if(data[0] == (int)(0x68)):
            print('reg:', reg,'who am i:', (data))
        time.sleep(1)
main()