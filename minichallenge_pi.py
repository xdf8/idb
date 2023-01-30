import time
import datetime
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

from functions import write_to_csv, write_data_to_api, load_yaml_file

DHT_PIN = 20  # rasperry pi Pin16, Grove D16
USR_PIN = 5
BUTTON_PIN = 16


def main():
    config = load_yaml_file("config.yaml")
    # keep track if button has been pressed
    button_pressed_prev = False
    try:
        # Initialize
        temp_sensor = dht.DHT("11", DHT_PIN)
        ultra_sonic_sensor = usr.GroveUltrasonicRanger(USR_PIN)
        button = GPIO(BUTTON_PIN, GPIO.IN)

        while True:
            if button.read():
                button_pressed_prev = True
                # measurements
                humidity, temperature = temp_sensor.read()
                distance = ultra_sonic_sensor.get_distance()

                # Print the temp_sensor values
                current_time = datetime.datetime.now()
                humidity = int(round(humidity))
                temperature = int(round(temperature))
                distance = int(round(distance))

                print(
                    "time: ",
                    current_time,
                    "temp: ",
                    temperature,
                    "hum: ",
                    humidity,
                    "distance: ",
                    distance,
                    # end="\r",
                )

                write_to_csv(
                    time=current_time,
                    temp=temperature,
                    hum=humidity,
                    dist=distance,
                )
                write_data_to_api(
                    temp=temperature,
                    hum=humidity,
                    dist=distance,
                    config=config,
                )
            # run after button has been released
            elif button.read() == 0 and button_pressed_prev:
                button_pressed_prev = False
                print("Measurement stopped by User")
                exit(0)

            else:
                print("Press button to start measuring!", end="\r")

            time.sleep(2)

    except KeyboardInterrupt:
        print("\nMeasurement stopped by User")
        exit(0)


if __name__ == "__main__":
    main()
