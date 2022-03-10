import time
from grove.button.button import Button


BUTTON_PIN = 16

def main():
    # Initialize
    button = Button(BUTTON_PIN)

    while True:
        if button.is_pressed():
            print('button is pressed', end = '\r')
            time.sleep(1)
        
        else:
            print('press the button!', end = '\r')
            time.sleep(1)

if __name__ == '__main__':
    main()