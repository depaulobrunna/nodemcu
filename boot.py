# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()
print('boot')
'''def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('LIT', 'l17@2017')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
do_collect()'''