from machine import Pin
from time import sleep
import dht

sensor = dht.DHT22(Pin(17))

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print("Temperature: {:.2f}°C Humidity: {:.2f}%".format(temp, hum))
    sleep(2)
