import time
# check, that python lib 'grove' is installed; pip3 freeze | grep grove
import grove.grove_temperature_humidity_sensor as dht
import grove.grove_ultrasonic_ranger as usr

DHT_PIN = 16 # rasperry pi Pin16, Grove D16
USR_PIN = 5


def main():
    # Initialize
    temp_sensor = dht.DHT("11", DHT_PIN)
    ultra_sonic_sensor = usr.GroveUltrasonicRanger(USR_PIN)

    try:
        # Try to grab a temp_sensor reading
        humidity, temperature = temp_sensor.read()
        distance = ultra_sonic_sensor.get_distance()

        # Print the temp_sensor values
        now = time.time()
        t = time.localtime(now)
        humidity = int(round(humidity))
        temperature = int(round(temperature))
        #print("{:02d}:{:02d}:{:02d},{:g},{:g}".format(t.tm_hour, t.tm_min, t.tm_sec, temperature, humidity), flush=True)
        print('temp: ', temperature)
        print('hum: ', humidity)
        print('distance: ', distance)


    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()