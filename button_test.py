import time
import grove.grove_button as button


BUTTON_PIN = 16

def main():
    # Initialize
    button = button.Button(BUTTON_PIN)

    while True:
        if button.is_pressed():
            print('button is pressed', end = '\r')
            time.sleep(1)
        
        else:
            print('press the button!', end = '\r')
            time.sleep(1)

if __name__ == '__main__':
    main()