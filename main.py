import esp
from machine import Pin
import time

def main():
    p5 = Pin(5, Pin.IN)    
    while(True):
        print(p5.value())
        
if __name__ == '__main__':
    print("main entered")
    esp.osdebug(0)
    main()