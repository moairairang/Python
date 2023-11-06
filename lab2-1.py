from machine import Pin
import time

p2 = Pin(2,Pin.OUT)


while(1):
    p2.on()
    time.sleep_ms(1000)
    p2.off()
    