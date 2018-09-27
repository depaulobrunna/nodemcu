import esp
from machine import Pin
import time

def main():
    pin = Pin(5, Pin.OUT)
    for i in range(10):
        pin.on()
        time.sleep_ms(500)
        pin.off()
        time.sleep_ms(500)
        print(i)
        
if __name__ == '__main__':
    print("main entered")
    main()