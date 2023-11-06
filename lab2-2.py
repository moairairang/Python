from machine import Pin
import time

p2 = Pin(2,Pin.OUT)
p3 = Pin(3,Pin.OUT)
p4 = Pin(4,Pin.OUT)

while(1<0):
    p2.on()
    time.sleep_ms(1000)
    p2.off()
    p3.on()
    time.sleep_ms(1000)
    p3.off()
    p4.on()
    time.sleep_ms(1000)
    p4.off()
    
    
