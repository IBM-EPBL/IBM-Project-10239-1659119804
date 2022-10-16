
#blink leds

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
from gpiozero import Button, TrafficLights, Buzzer    
from time import sleep    

def blink_led():
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
    while True: # Run forever
     GPIO.output(8, GPIO.HIGH) # Turn on
     sleep(1) # Sleep for 1 second
     GPIO.output(8, GPIO.LOW) # Turn off
     sleep(1) # Sleep for 1 second

#traffic light


def traffic_light():
    buzzer = Buzzer(15)    
    button = Button(21)    
    lights = TrafficLights(25, 8, 7)    
        
    while True:    
               button.wait_for_press()   
               buzzer.on()   
               lights.green.on()    
               sleep(1)    
               lights.amber.on()    
               sleep(1)    
               lights.red.on()    
               sleep(1)    
               lights.off()   
               buzzer.off()  

def main():
    a=input("Enter 1 to run blink_led code or 2 to run traffic light led code!")
    if a==1:
        blink_led()
    elif a==2:
        traffic_light()
main()
