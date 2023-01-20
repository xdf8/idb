import time
# check, that python lib 'grove' is installed; pip3 freeze | grep grove
import grove.grove_temperature_humidity_sensor as dht
import grove.grove_ultrasonic_ranger as usr
from grove.gpio import GPIO

import os
import csv

DHT_PIN = 20 # rasperry pi Pin16, Grove D16
USR_PIN = 5
BUTTON_PIN = 16

def main():
    # Initialize
    temp_sensor = dht.DHT("11", DHT_PIN)
    ultra_sonic_sensor = usr.GroveUltrasonicRanger(USR_PIN)
    button = GPIO(BUTTON_PIN, GPIO.IN)

    while True:
        if button.read():
            # measurements
            humidity, temperature = temp_sensor.read()
            distance = ultra_sonic_sensor.get_distance()

            # Print the temp_sensor values
            now = time.time()
            current_time = time.localtime(now)
            humidity = int(round(humidity))
            temperature = int(round(temperature))
            distance = int(round(distance))
            
            print(
                'temp: ', temperature,
                'hum: ', humidity,
                'distance: ', distance,
                end = '\r'
                )
            
            # write to file
            writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            # add csv header
            writer.writerow(['timestamp', 'temperature', 'humidity', 'distance'])
            with open('measurements_pi/data.csv', 'a') as csvfile:
                # add data
                writer.writerow([f'{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}', temperature, humidity, distance])

        else:
            print('Press button to start measuring!', end = '\r')
        
        time.sleep(1)

if __name__ == '__main__':
    main()