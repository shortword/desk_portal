import board
import busio
from adafruit_esp32spi import adafruit_esp32spi
from adafruit_adt7410 import ADT7410

import analogio
import digitalio

import neopixel
import time

# WiFi Globals
esp32_cs =      digitalio.DigitalInOut(board.ESP_CS)
esp32_busy =    digitalio.DigitalInOut(board.ESP_BUSY)
esp32_reset =   digitalio.DigitalInOut(board.ESP_RESET)
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_busy, esp32_reset)

# Ambient light sensor
ald = analogio.AnalogIn(board.LIGHT)

# Temperature sensor
temp = ADT7410(busio.I2C(board.SCL, board.SDA), address=0x48)

# NeoPixel
np = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.0)
np[0] = 0x0 # Set to black

def setBacklight():
    board.DISPLAY.brightness = min(1.0, (ald.value / 65535) + 0.1)
    print("Backlight: ", board.DISPLAY.brightness)

# Board init


# "Main" Loop
while True:
    setBacklight()
    print("Temp: %s C" % temp.temperature)
    time.sleep(5)
