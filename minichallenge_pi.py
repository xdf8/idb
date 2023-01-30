import time
import os
import csv

import grove.grove_ultrasonic_ranger as usr
from grove.gpio import GPIO

try:
    import grove.grove_temperature_humidity_sensor as dht
except:
    # Install  pip3 install seeed-python-dht if ModuleNotFoundError: No module named 'grove.grove_temperature_humidity_sensor'
    # check, that python lib 'seeed-python-dht' is installed; sudo pip3 install seeed-python-dht
    import seeed_dht as dht

from functions import write_to_csv, write_data_to_api

DHT_PIN = 20  # rasperry pi Pin16, Grove D16
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
                "temp: ",
                temperature,
                "hum: ",
                humidity,
                "distance: ",
                distance,
                end="\r",
            )
            # use current date and time as filename
            filename = f"data/{time.strftime('%Y-%m-%d_%H-%M-%S', current_time)}.csv"
            write_to_csv(
                temp=temperature, hum=humidity, dist=distance, file_name=filename
            )
            write_data_to_api(
                temp=temperature, hum=humidity, dist=distance, config_path="config.yaml"
            )

        else:
            print("Press button to start measuring!", end="\r")

        time.sleep(1)


if __name__ == "__main__":
    main()
