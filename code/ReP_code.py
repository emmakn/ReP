#!/user/bin/env python
import RPi.GPIO as GPIO
import time

# set up pins
in1 = 24
in2 = 23
en = 25

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(en,GPIO.OUT)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)

def print_message():
    print("\nl-loop s-stop u-up d-down Ctrl+C-quit\n")

def destroy():
    GPIO.output(en,GPIO.LOW)
    GPIO.cleanup()

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

if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()