import time
import grove.grove_button as button
from grove.gpio import GPIO

BUTTON_PIN = 16

def main():
    # Initialize
    button = GPIO(BUTTON_PIN, GPIO.IN)

    while True:
        if button.is_pressed():
            print('button is pressed', end = '\r')
            time.sleep(1)
        
        else:
            print('press the button!', end = '\r')
            time.sleep(1)

if __name__ == '__main__':
    main()