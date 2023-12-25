from machine import Pin, I2C
from time import sleep
import dht
import ssd1306

# Configure the OLED display
i2c = I2C(0, scl=Pin(5), sda=Pin(4))  # Adjust the I2C bus index and pin numbers based on your connections
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Configure the DHT22 sensor
sensor_pin = Pin(17)
sensor = dht.DHT22(sensor_pin)

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()

    # Display on OLED
    oled.fill(0)  # Clear the display
    oled.text("Temperature: {:.2f}C".format(temp), 0, 0)
    oled.text("Humidity: {:.2f}%".format(hum), 0, 16)
    oled.show()

    # Print to console
    print("Temperature: {:.2f}°C Humidity: {:.2f}%".format(temp, hum))

    sleep(2)
