# Code

ReP_code.py is broken up into an intro and 5 functinos.

## Intro
~~~
#!/user/bin/env python
import RPi.GPIO as GPIO
import time

# set up pins
in1 = 24
in2 = 23
en = 25
~~~
The intro defines the environment, imports the GPIO and time libraries, and defines the pins used.

## Function 1: setup
~~~
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(en,GPIO.OUT)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
~~~
The setup function defines the pins as BCM and outputs and sets them to "off" (LOW) to start.

## Function 2: print_message
~~~
def print_message():
    print("\nl-loop s-stop u-up d-down Ctrl+C-quit\n")
~~~
These are the 5 keyboard commands that can be used in the program to run different commands. This is the messasge printed in the terminal for the user to see and use as a reference.

## Function 3: destroy
~~~
def destroy():
    GPIO.output(en,GPIO.LOW)
    GPIO.cleanup()
~~~
This will end the program.

## Function 4: main
~~~
def main():
    print_message()
    p=GPIO.PWM(en,1000)
    p.start(50) # motor does not consistently work below 50
    try:
        while(1):
            x = raw_input()
            if x=='l':
                for i in range(300): # 100 equals 5 minutes
                    print("cycle " + str(i+1))
                    # up
                    p.ChangeDutyCycle(50)
                    GPIO.output(in1,GPIO.LOW)
                    GPIO.output(in2,GPIO.HIGH)
                    time.sleep(1.15)
                    # down
                    p.ChangeDutyCycle(55)
                    GPIO.output(in1,GPIO.HIGH)
                    GPIO.output(in2,GPIO.LOW)
                    time.sleep(1.3)
                    # pause
                    GPIO.output(in1,GPIO.LOW)
                    time.sleep(.55)
                x=='z'
            elif x=='s':
                print("stop")
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.LOW)
                x=='z'
            elif x=='u':
                print("up")
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.HIGH)
                x=='z'
            elif x=='d':
                print("down")
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                x=='z'
            else:
                print("that is not a recognized command, please use one of the commands listed below:\n")
                print_message()
    except KeyboardInterrupt:
        destroy()
~~~
This is the main code that is run when the program is initiated. It contains the 3 previously defined functions. The two settings that are mainly used to calibrate the code to a given pipette are:
~~~
p.ChangeDutyCycle()
time.sleep()
~~~
The DutyCycle determines the percentage of power given to the motor. Our motor did not work consistently below 50% power. The more power that is supplied, the faster the motor goes. The sleep time determines how long each command runs. Between these two commands you can determine speed and duration.

The loop command was developed with the intent to breakup parasitic worms in solution down to the cellular level. The protocol required the solution to be mixed at a consistent rate of one repetition per 3 seconds (or 100 reps per 5 min) for at least 15 minutes.

The stop command stops the motor without exiting the program.

The up and down commands move the plunger up and down.

KeyboardInterrupt is Ctrl+C which exits the entire program.

## Function 5: __name__ = '__main__'
~~~
if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()
~~~
This function will run the main function when the following command is entered in the terminal:
~~~
sudo python ReP_code.py
~~~
