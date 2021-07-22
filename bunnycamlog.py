# Source code from Adafruit Howtpo, 2021 ladyada for Adafruit Industries  
# https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup, License: MIT License 
# 
# Changes and additions for bunnycam, 2021 Henning 'haenno' Beier, haenno@web.de
# Part of https://github.com/haenno/bunnycam
#  

import time
import board
import adafruit_dht
from datetime import datetime

# Sensor data pin = D4
s= adafruit_dht.DHT22(board.D4)
while True:
    try:
        t = s.temperature
        h = s.humidity
        now = datetime.now()
        dt_string = now.strftime("&#x1F4C5 %d/%m/%Y &#x23F2 %H:%M:%S")
        f = open("/home/pi/bunnycam/bunnycam.log", "a")
        f.write("{} &#8594 &#x1F321 {:.1f} &#176C  &#x1F30A {} % \n".format(dt_string, t, h))
        f.close()
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        time.sleep(2.5)
        continue
    except Exception as error:
        s.exit()
        raise error
    time.sleep(60)
